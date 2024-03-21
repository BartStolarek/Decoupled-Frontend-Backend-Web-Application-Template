import pytest
from server.services.user import register_user, delete_user, update_user
from server.models.user import User
from server import db, create_server
from sqlalchemy.exc import IntegrityError
from unittest.mock import patch


class TestRegisterUser:
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.app = create_server('testing')
        with self.app.app_context():
            db.drop_all()  # Drop all tables
            db.create_all()  # Recreate tables
            
    
    @patch('server.services.user.db.session.add')
    @patch('server.services.user.db.session.commit')
    def test_success(self, mock_commit, mock_add):
        with self.app.app_context():
            # Arrange
            user_dict = {
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@example.com",
                "password": "password123"  # Ensure password is provided
            }

            # Act
            success, message = register_user(user_dict)
            
            # Assert
            assert success is True
            assert message == 'User registered successfully'
            mock_add.assert_called_once()
            mock_commit.assert_called_once()

    @patch('server.services.user.db.session.add')
    @patch('server.services.user.db.session.commit')
    @patch('server.services.user.db.session.rollback')
    def test_integrity_error(self, mock_rollback, mock_commit, mock_add):
        with self.app.app_context():
            # Arrange
            user_dict = {
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@example.com",
                "password": "password123"
            }

            # Create a mock IntegrityError
            error = IntegrityError(params={}, orig=Exception("UNIQUE constraint failed: users.email"), statement="")
            mock_add.side_effect = error

            # Act
            success, message = register_user(user_dict)

            # Assert
            assert success is False
            assert 'Integrity Error: User with that email already exists' in message
            mock_add.assert_called_once()
            mock_commit.assert_not_called()
            mock_rollback.assert_called_once()

    @patch('server.services.user.db.session.add')
    @patch('server.services.user.db.session.commit')
    @patch('server.services.user.db.session.rollback')
    def test_unexpected_error(self, mock_rollback, mock_commit, mock_add):
        with self.app.app_context():
            # Arrange
            user_dict = {
                "first_name": "Alice",
                "last_name": "Doe",
                "email": "alice.doe@example.com",
                "password": "password123"
            }
            error = Exception("Unexpected error")
            mock_add.side_effect = error
            
            # Act
            success, message = register_user(user_dict)
            
            # Assert
            assert success is False
            assert 'Unexpected error occured. Could not register user' in message
            mock_add.assert_called_once()
            mock_commit.assert_not_called()
            mock_rollback.assert_called_once()


class TestDeleteUser:
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.app = create_server('testing')
        with self.app.app_context():
            db.drop_all()  # Drop all tables
            db.create_all()  # Recreate tables
            # Create a user for testing deletion
            test_user = User(first_name="Test", last_name="User", email="test@example.com", password="password")
            db.session.add(test_user)
            db.session.commit()

    @patch('server.services.user.db.session.delete')
    @patch('server.services.user.db.session.commit')
    def test_success(self, mock_commit, mock_delete):
        with self.app.app_context():
            # Arrange
            user_dict = {"email": "test@example.com"}

            # Act
            success, message = delete_user(user_dict)
            
            # Assert
            assert success is True
            assert message == 'User deleted successfully'
            mock_delete.assert_called_once()
            mock_commit.assert_called_once()

    @patch('server.services.user.db.session.delete')
    @patch('server.services.user.db.session.commit')
    def test_delete_nonexistent_user(self, mock_commit, mock_delete):
        with self.app.app_context():
            # Arrange
            user_dict = {"email": "nonexistent@example.com"}

            # Act
            success, message = delete_user(user_dict)
            
            # Assert
            assert success is False
            assert message == 'User does not exist'
            mock_delete.assert_not_called()
            mock_commit.assert_not_called()

    @patch('server.services.user.db.session.delete')
    @patch('server.services.user.db.session.commit')
    @patch('server.services.user.db.session.rollback')
    def test_unexpected_error(self, mock_rollback, mock_commit, mock_delete):
        with self.app.app_context():
            # Arrange
            user_dict = {"email": "test@example.com"}
            mock_delete.side_effect = Exception("Unexpected error")

            # Act
            success, message = delete_user(user_dict)
            
            # Assert
            assert success is False
            assert 'Unexpected error occured. Could not delete user' in message
            mock_delete.assert_called_once()
            mock_commit.assert_not_called()
            mock_rollback.assert_called_once()
            
class TestUpdateUser:
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.app = create_server('testing')
        with self.app.app_context():
            db.drop_all()  # Drop all tables
            db.create_all()  # Recreate tables
            # Create users for testing update
            test_user1 = User(first_name="Existing", last_name="User", email="existing@example.com", password="password")
            test_user2 = User(first_name="Another", last_name="User", email="another@example.com", password="password")
            db.session.add_all([test_user1, test_user2])
            db.session.commit()

    @patch('server.services.user.db.session.commit')
    def test_update_success(self, mock_commit):
        with self.app.app_context():
            # Arrange
            user_dict = {
                "email": "existing@example.com",
                "first_name": "UpdatedFirstName"
            }
            
            # Act
            success, message = update_user(user_dict)

            # Assert
            assert success is True
            assert message == 'User updated successfully'
            mock_commit.assert_called_once()

    @patch('server.services.user.db.session.commit')
    def test_update_nonexistent_user(self, mock_commit):
        with self.app.app_context():
            # Arrange
            user_dict = {
                "email": "nonexistent@example.com",
                "first_name": "UpdatedFirstName"
            }

            # Act
            success, message = update_user(user_dict)

            # Assert
            assert success is False
            assert message == 'User does not exist'
            mock_commit.assert_not_called()

    @patch('server.services.user.db.session.commit')
    @patch('server.services.user.db.session.rollback')
    @patch('server.services.user.db.session.merge')
    def test_update_integrity_error(self, mock_merge, mock_rollback, mock_commit):
        with self.app.app_context():
            # Arrange
            user_dict = {
                "email": "existing@example.com",
                "new_email": "another@example.com"  # Assume this email already exists
            }
            error = IntegrityError(params={}, orig=Exception("UNIQUE constraint failed: users.email"), statement="")
            mock_merge.side_effect = error  

            # Act
            success, message = update_user(user_dict)

            # Assert
            assert success is False
            assert 'Integrity Error: User with that email already exists' in message
            mock_merge.assert_called_once()
            mock_rollback.assert_called_once()

    @patch('server.services.user.db.session.commit')
    @patch('server.services.user.db.session.rollback')
    @patch('server.services.user.db.session.merge')
    def test_update_unexpected_error(self, mock_merge, mock_rollback, mock_commit):
        with self.app.app_context():
            # Arrange
            user_dict = {
                "email": "existing@example.com",
                "first_name": "UpdatedFirstName"
            }
            error = Exception("Unexpected error")
            mock_merge.side_effect = error

            # Act
            success, message = update_user(user_dict)

            # Assert
            assert success is False
            assert 'Unexpected error occurred. Could not update user' in message
            mock_merge.assert_called_once()
            mock_rollback.assert_called_once()


   