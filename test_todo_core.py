import unittest
import todo_core


class TodoCoreTests(unittest.TestCase):
    def setUp(self):
        todo_core.reset_tasks()

    def test_create_read_update_delete(self):
        first = todo_core.add_task("Learn Python")
        self.assertEqual(first["id"], 1)
        self.assertEqual(todo_core.get_tasks()[0]["title"], "Learn Python")

        updated = todo_core.update_task(1, title="Practice Python", completed=True)
        self.assertEqual(updated["title"], "Practice Python")
        self.assertTrue(updated["completed"])

        removed = todo_core.remove_task(1)
        self.assertEqual(removed["id"], 1)
        self.assertEqual(todo_core.get_tasks(), [])

    def test_invalid_task_title(self):
        with self.assertRaises(ValueError):
            todo_core.add_task("   ")

    def test_missing_task(self):
        self.assertIsNone(todo_core.get_task(99))
        self.assertIsNone(todo_core.update_task(99, title="Missing"))
        self.assertIsNone(todo_core.remove_task(99))


if __name__ == "__main__":
    unittest.main()
