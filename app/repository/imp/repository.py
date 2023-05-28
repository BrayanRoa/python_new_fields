from app.repository.abstract_repository import AbstractRepository
from app.db import db 
from sqlalchemy import text
from sqlalchemy.sql import or_
from datetime import datetime
from flask import g
import json
import logging

class Repository(AbstractRepository):
    
    def __init__(self, model_cls):
        self.session = db.session
        self.model_cls = model_cls  
        
    def add(self, model):        
        try:
            # setattr(model,"created_at", datetime.now())
            # setattr(model,"updated_at",datetime.now())
            self.session.add(model)
        except Exception as e:
            logging.error(str(e))
            self.session.add(model)
            self.session.commit()
            # self.addAudit(model.id, self.model_cls.__tablename__, model ,"ADD")
            return model
        
        self.session.commit()
        # self.addAudit(model.id, self.model_cls.__tablename__, model ,"ADD")
        return model

    def list(self, page, per_page,param=or_(),order=None):
        model_paginate = self.session.query(self.model_cls).filter(param).paginate(page=page, per_page=per_page)
        meta = {
            "page": model_paginate.page,
            "pages": model_paginate.pages,
            "total_count": model_paginate.total,
            "prev_page": model_paginate.prev_num,
            "next_page": model_paginate.next_num,
            "has_next": model_paginate.has_next,
            "has_prev": model_paginate.has_prev,
        }
        
        return model_paginate.items,meta
    
    def get(self, id_):
        obj = self.session.query(self.model_cls).get(id_)
        if obj == None:
            return None
        if getattr(obj, "deleted_at") is not None:
            return None
        return obj
    
    def exist(self, id_):
        obj = self.get(id_)
        if obj == None:
            return False
        return True

    def update(self, id_, fields):
        obj = self.get(id_)
        if getattr(obj,"updated_at" , "") != "":
            setattr(obj,"updated_at", datetime.now())
            
        for field, value in fields.items():
            obj.__setattr__(field, value)
        self.session.commit()
        
        self.addAudit(id_, self.model_cls.__tablename__,fields,"UPDATE")
        return obj

    def delete(self, id_):
        model = self.get(id_)
        setattr(model,"deleted_at", datetime.now())
        self.addAudit(id_, self.model_cls.__tablename__,model,"DELETE")
        self.session.commit()