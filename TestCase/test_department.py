# -*- Coding: utf-8 -*-
# Author: Yu
from api_Po.department import Department_po


class TestDepartment:

    def test_creat(self):
        r = Department_po.creat_department("yu", "1")
        print(r)
        assert r["errmsg"] == "created"

    def test_update(self):
        r = Department_po.update_department("2", name="yu_new")
        print(r)
        assert r["errmsg"] == "updated"

    def test_list(self):
        r = Department_po.list_department()
        print(r)
        assert r["errmsg"] == "ok"

    def test_delete(self):
        r = Department_po.del_department("2")
        print(r)
        assert r["errmsg"] == "deleted"
