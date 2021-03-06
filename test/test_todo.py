# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase
from odoo.exceptions import AccessError


class TestTodo(TransactionCase):

    def test_create(self):
        """Create a simple Todo"""
        todo = self.env['todoroc_app.todoroc_app']
        task = todo.create({'name': 'Test Task'})
        self.assertEqual(task.is_done, False)

        # Test Toggle Done
        task.do_toggle_done()
        self.assertTrue(task.is_done)
        # Test Clear Done
        todo.do_clear_done()
        self.assertFalse(task.active)

    def setUp(self, *args, **kwargs):
        result = super(TestTodo, self).setUp(*args, **kwargs)
        user_demo = self.env.ref('base.user_demo')
        self.env= self.env(user=user_demo)
        return result

    def test_record_rule(self):
        "Test per user record rules"
        Todo = self.env['todoroc_app.todoroc_app']
        task = Todo.sudo().create({'name': 'Admin Task'})
        with self.assertRaises(AccessError):
            Todo.browse([task.id]).name