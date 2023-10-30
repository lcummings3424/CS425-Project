-- Users Table
CREATE TABLE
    users (
        user_id INTEGER UNIQUE PRIMARY KEY,
        first_name TEXT NOT NULL,
        middle_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        hashed_password TEXT NOT NULL,
        join_date DATE DEFAULT CURRENT_DATE,
        phone INTEGER UNIQUE
    );

-- Area of Focus Table
CREATE TABLE
    area_of_focus (
        area_name TEXT NOT NULL, 
         description TEXT
    );

-- Content type details table 
CREATE TABLE
    content_type_details (
        content_type_id INTEGER PRIMARY KEY,
        content_type_title TEXT NOT NULL,
        description TEXT
    );

-- Content Table
CREATE TABLE
    contents (
        content_id INTEGER PRIMARY KEY,
        content_title TEXT NOT NULL,
        description TEXT
    );

-- Content type table 
CREATE TABLE
    content_type (
        content_type_id INTEGER PRIMARY KEY REFERENCES content_type_details (content_type_id),
        content_id INTEGER PRIMARY KEY REFERENCES contents (content_id),
        media_type TEXT NOT NULL
    );

-- Content focus table
CREATE TABLE
    content_focus (
        area_name TEXT PRIMARY KEY REFERENCES area_of_focus (area_name),
        content_id INTEGER PRIMARY KEY REFERENCES contents (content_id)
    );

-- Quizzes Table
CREATE TABLE
    quizzes (
        quiz_id INTEGER PRIMARY KEY,
        passing_score INTEGER,
        quiz_type TEXT NOT NULL CHECK (quiz_type IN ('placement', 'practice', 'final')),
        time_limit INTEGER
    );

-- Quiz content type Table 
CREATE TABLE
    quiz_content_type (
        quiz_id INTEGER PRIMARY KEY REFERENCES quizzes (quiz_id),
        content_type_id INTEGER PRIMARY KEY REFERENCES content_type_details (content_type_id)
    );

-- Questions Table
CREATE TABLE
    questions (
        question_id INTEGER PRIMARY KEY,
        question_content TEXT NOT NULL,
        option_a TEXT,
        option_b TEXT,
        option_c TEXT,
        correct_option CHAR(1) CHECK (correct_option IN ('A', 'B', 'C')),
        answer_explanation TEXT
    );

-- Quiz has questions table
CREATE TABLE
    has_questions (
        question_id INTEGER PRIMARY KEY REFERENCES questions (question_id),
        quiz_id INTEGER PRIMARY KEY REFERENCES quizzes (quiz_id),
        total_questions INTEGER
    );

-- Flashcard Sets Table
CREATE TABLE
    flashcards (
        flashcard_id INTEGER PRIMARY KEY,
        question TEXT NOT NULL,
        answer TEXT NOT NULL,
        answer_explanation TEXT
    );

-- Flashcard content type table
CREATE TABLE
    flashcard_content_type (
        flashcard_id INTEGER PRIMARY KEY REFERENCES flashcards (flashcard_id),
        content_type_id INTEGER PRIMARY KEY REFERENCES content_type_details (content_type_id)
    );

-- Quiz taken table 
CREATE TABLE
    taken (
        user_id INTEGER PRIMARY KEY REFERENCES users (user_id),
        quiz_id INTEGER PRIMARY KEY quizzes (quiz_id),
        score INTEGER,
        letter_grade CHAR(1) CHECK (letter_grade IN ('A', 'B', 'C', 'D', 'F'))
    );

-- Referred table
CREATE TABLE
    referred (
        user_id INTEGER PRIMARY KEY REFERENCES users (user_id),
        referred_by INTEGER PRIMARY KEY
    );