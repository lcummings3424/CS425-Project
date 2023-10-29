-- Users Table
CREATE TABLE
    users (
        user_id INTEGER PRIMARY KEY,
        user_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        hashed_password TEXT NOT NULL,
        join_date DATE DEFAULT CURRENT_DATE,
        phone INTEGER UNIQUE
    );

-- Area of Focus Table
CREATE TABLE
    area_of_focus (
        focus_area_id INTEGER PRIMARY KEY,
        area_name TEXT NOT NULL,
        description TEXT
    );

-- Type of Content Table
CREATE TABLE
    content_type (
        content_type_id INTEGER PRIMARY KEY,
        focus_area_id INTEGER REFERENCES area_of_focus (focus_area_id),
        content_type_title TEXT NOT NULL,
        description TEXT
    );

-- Content Table
CREATE TABLE
    contents (
        content_id INTEGER PRIMARY KEY,
        content_type_id INTEGER REFERENCES content_type (content_type_id),
        media_type TEXT NOT NULL,
        content_title TEXT NOT NULL,
        description TEXT
    );

-- Quizzes Table
CREATE TABLE
    quizzes (
        quiz_id INTEGER PRIMARY KEY,
        content_type_id INTEGER REFERENCES content_type (content_type_id),
        total_questions INTEGER,
        passing_score INTEGER,
        quiz_type TEXT NOT NULL CHECK (quiz_type IN ('placement', 'practice', 'final')),
        time_limit INTEGER
    );

-- Questions Table
CREATE TABLE
    questions (
        question_id INTEGER PRIMARY KEY,
        content TEXT NOT NULL,
        option_a TEXT,
        option_b TEXT,
        option_c TEXT,
        correct_option CHAR(1) CHECK (correct_option IN ('A', 'B', 'C')),
        quiz_id INTEGER REFERENCES quizzes (quiz_id),
        answer_explanation TEXT
    );

-- Flashcard Sets Table
CREATE TABLE
    flashcards (
        flashcard_id INTEGER PRIMARY KEY,
        content_type_id INTEGER REFERENCES content_type (content_type_id),
        question TEXT NOT NULL,
        answer TEXT NOT NULL
    );

-- Quiz taken table 
CREATE TABLE 
    taken (
        user_id INTEGER PRIMARY KEY REFERENCES users (user_id),
        quiz_id INTEGER REFERENCES quizzes (quiz_id),
        date_taken DATE DEFAULT CURRENT_DATE        
    )

-- Quiz scores Table
CREATE TABLE
    quiz_scores (
        quiz_id INTEGER REFERENCES quizzes (quiz_id),
        score INTEGER,
    );