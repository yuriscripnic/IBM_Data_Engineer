import unittest
import ast
import os

class TestETLDagStatic(unittest.TestCase):
    def setUp(self):
        """Parse the DAG file into an Abstract Syntax Tree."""
        # Correct the path to be relative to the project root
        dag_file_path = os.path.join(os.path.dirname(__file__), '..', 'ETL_toll_data.py')
        with open(dag_file_path, 'r') as f:
            self.file_content = f.read()
        self.tree = ast.parse(self.file_content)

    def test_dag_definition(self):
        """Test that the DAG is defined with the correct ID."""
        dag_defined = False
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == 'dag':
                        if isinstance(node.value, ast.Call):
                            if isinstance(node.value.func, ast.Name) and node.value.func.id == 'DAG':
                                for keyword in node.value.keywords:
                                    if keyword.arg == 'dag_id' and isinstance(keyword.value, ast.Constant) and keyword.value.value == 'ETL_toll_data':
                                        dag_defined = True
        self.assertTrue(dag_defined, "DAG 'ETL_toll_data' not found or not correctly defined.")

    def test_task_definitions(self):
        """Test if all expected tasks are defined as BashOperator."""
        expected_task_ids = {
            'unzip_data',
            'extract_data_from_csv',
            'extract_data_from_tsv',
            'extract_data_from_fixed_width',
            'consolidate_data',
            'transform_data'
        }
        found_tasks = set()
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Assign):
                if isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name) and node.value.func.id == 'BashOperator':
                    for keyword in node.value.keywords:
                        if keyword.arg == 'task_id' and isinstance(keyword.value, ast.Constant):
                            found_tasks.add(keyword.value.value)
        
        self.assertSetEqual(found_tasks, expected_task_ids)

    def test_task_dependencies(self):
        """Test the dependencies between tasks by checking the last line."""
        # This is a simplified check. A more robust check would parse the dependency chain.
        last_line = self.file_content.strip().split('\n')[-1]
        expected_dependency_chain = "unzip_data >> [extract_data_from_csv, extract_data_from_tsv, extract_data_from_fixed_width] >> consolidate_data >> transform_data"
        self.assertEqual(last_line.strip(), expected_dependency_chain)

if __name__ == '__main__':
    unittest.main()