CREATE TABLE IF NOT EXISTS UserGroup (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS UserSubject (
    id INT PRIMARY KEY AUTO_INCREMENT,
    userID INT NOT NULL,
    subjectID INT NOT NULL,
    FOREIGN KEY (userID) REFERENCES User(id),
    FOREIGN KEY (subjectID) REFERENCES Subject(id)
);

CREATE TABLE IF NOT EXISTS UserRole (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS User (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    lastName VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE,
    groupID INT NOT NULL,
    roleID INT NOT NULL,
    FOREIGN KEY (groupID) REFERENCES UserGroup(id),
    FOREIGN KEY (roleID) REFERENCES UserRole(id)
);

CREATE TABLE IF NOT EXISTS Subject (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    room VARCHAR(255) NOT NULL,
    teacherID INT NOT NULL,
    weekday INT NOT NULL,
    startTime TIME NOT NULL,
    endTime TIME NOT NULL,
    FOREIGN KEY (teacherID) REFERENCES User(id)
);

CREATE TABLE IF NOT EXISTS Assistance (
    id INT PRIMARY KEY AUTO_INCREMENT,
    studentID INT NOT NULL,
    teacherID INT NOT NULL,
    subjectID INT NOT NULL,
    assistance_status ENUM('present', 'absent', 'justified') NOT NULL,
    date DATETIME DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (studentID, subjectID, date),
    FOREIGN KEY (studentID) REFERENCES User(id),
    FOREIGN KEY (teacherID) REFERENCES User(id),
    FOREIGN KEY (subjectID) REFERENCES Subject(id)
);
