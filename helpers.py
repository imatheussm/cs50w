from flask_login._compat import PY2, text_type

class User(object):
    """
    A User class, which stores the user's data in order to make
    log-in operations and database queries. It is based on
    flask-login's mixins.

    Flask description:
        This provides default implementations for the methods that
        Flask-Login expects user objects to have.
    """

    def __init__(self, identity, username, password, gender, firstName, lastName, isActive=True, isAuthenticated=True, isAnonymous=False):
        """
        Initializes a User instance with the id provided.
        """
        self.userID = identity
        self.username = username
        self.password = password
        self.gender = gender
        self.firstName = firstName
        self.lastName = lastName
        self.has_picture = os.path.exists(f"./static/userPictures/{str(self.userID)}.jpg")

        self.is_active = isActive
        self.is_authenticated = isAuthenticated
        self.is_anonymous = isAnonymous

        # Re-stablish database connection
        connection, db = stablishConnection("./kanban.db")

        # Get to-do task number
        db.execute("SELECT * FROM tasks\
                   WHERE (creatorUserID = :userID\
                   OR responsibleUserID = :userID)\
                   AND status = 'To-do'",
                   {"userID": self.userID})
        query = db.fetchall()
        self.todo = len(query)

        # Get doing task number
        db.execute("SELECT * FROM tasks\
                   WHERE (creatorUserID = :userID\
                   OR responsibleUserID = :userID)\
                   AND status = 'Doing'",
                   {"userID": self.userID})
        query = db.fetchall()
        self.doing = len(query)

        # Get done task number
        db.execute("SELECT * FROM tasks\
                   WHERE (creatorUserID = :userID\
                   OR responsibleUserID = :userID)\
                   AND status = 'Done'",
                   {"userID": self.userID})
        query = db.fetchall()
        self.done = len(query)

        # Close connection and delete query
        del(query)
        connection.close()

    if not PY2:  # pragma: no cover
        # Python 3 implicitly set __hash__ to None if we override __eq__
        # We set it back to its default implementation
        __hash__ = object.__hash__

    def isActive(self):
        """
        Returns if the user is active or not.
        """
        return self.is_active

    def get_gender(self):
        """
        Returns the user's gender
        """
        return self.gender

    def get_picture_status(self):
        """
        Returns if a user has a picture
        """
        return self.has_picture

    def get_id(self):
        """
        Returns the user's id
        """
        return self.userID

    def __eq__(self, other):
        '''
        Checks the equality of two `UserMixin` objects using `get_id`.
        '''
        if isinstance(other, User):
            return self.get_id() == other.get_id()
        return NotImplemented

    def __ne__(self, other):
        '''
        Checks the inequality of two `UserMixin` objects using `get_id`.
        '''
        equal = self.__eq__(other)
        if equal is NotImplemented:
            return NotImplemented
        return not equal


class AnonymousUser(object):
    '''
    This is the default object for representing an anonymous user.
    '''

    def is_authenticated(self):
        """
        Returns if the user is authenticated or not.
        """
        return False

    def is_active(self):
        """
        Returns if the user is active or not.
        """
        return False

    def is_anonymous(self):
        """
        Returns if the user is anonymous or not.
        """
        return True

    def get_id(self):
        return 0