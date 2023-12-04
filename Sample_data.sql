-- Users Table
INSERT INTO
    users (
        user_id,
        first_name,
        middle_name,
        last_name,
        email,
        hashed_password,
        join_date,
        joined_time,
        phone
    )
VALUES
    (
        1,
        'John',
        'M',
        'Doe',
        'john.doe@email.com',
        'hashedpass1',
        '2023-01-01',
        '12:00:00',
        1234567890
    ),
    (
        2,
        'Jane',
        NULL,
        'Smith',
        'jane.smith@email.com',
        'hashedpass2',
        '2023-02-01',
        '14:30:00',
        9876543210
    ),
    (
        3,
        'Alice',
        'A',
        'Johnson',
        'alice.johnson@email.com',
        'hashedpass3',
        '2023-03-01',
        '10:45:00',
        5555555555
    ),
    (
        4,
        'Bob',
        'B',
        'Williams',
        'bob.williams@email.com',
        'hashedpass4',
        '2023-04-01',
        '18:15:00',
        1111111111
    ),
    (
        5,
        'Eva',
        NULL,
        'Brown',
        'eva.brown@email.com',
        'hashedpass5',
        '2023-05-01',
        '20:00:00',
        9999999999
    );

-- Area of Focus Table
INSERT INTO
    area_of_focus (area_name, description)
VALUES
    (
        'Programming',
        'Software development and programming languages'
    ),
    ('Science', 'Various scientific fields'),
    ('Art', 'Visual and performing arts'),
    ('Health', 'Health and wellness'),
    ('History', 'Historical events and periods');

-- Content type details table
INSERT INTO
    content_type_details (content_type_id, content_type_title, description)
VALUES
    (1, 'Article', 'Written content for reading'),
    (2, 'Video', 'Visual content for watching'),
    (3, 'Quiz', 'Questions and answers for assessment'),
    (
        4,
        'Flashcard',
        'Interactive flashcards for learning'
    ),
    (5, 'Book', 'Long-form written content');

-- Content Table
INSERT INTO
    contents (content_id, content_title, description)
VALUES
    (
        1,
        'Introduction to Programming',
        'Basic concepts and principles of programming'
    ),
    (
        2,
        'The Periodic Table',
        'Chemical elements and their properties'
    ),
    (
        3,
        'Art History Overview',
        'Major art movements and artists'
    ),
    (
        4,
        'Healthy Living Tips',
        'Guidance on maintaining a healthy lifestyle'
    ),
    (5, 'World War II', 'Historical events and impact');

-- Content type table
INSERT INTO
    content_type (content_type_id, content_id, media_type)
VALUES
    (1, 1, 'Article'),
    (2, 2, 'Video'),
    (3, 3, 'Quiz'),
    (4, 4, 'Flashcard'),
    (5, 5, 'Article');

-- Content focus table
INSERT INTO
    content_focus (area_name, content_id)
VALUES
    ('Programming', 1),
    ('Science', 2),
    ('Art', 3),
    ('Health', 4),
    ('History', 5);

-- Quizzes Table
INSERT INTO
    quizzes (quiz_id, passing_score, quiz_type, time_limit)
VALUES
    (1, 70, 'placement', 60),
    (2, 80, 'practice', 45),
    (3, 75, 'final', 75),
    (4, 60, 'placement', 45),
    (5, 85, 'practice', 60);

-- Quiz content type Table
INSERT INTO
    quiz_content_type (quiz_id, content_type_id)
VALUES
    (1, 3),
    (2, 3),
    (3, 3),
    (4, 3),
    (5, 3);

-- Questions Table
INSERT INTO
    questions (
        question_id,
        question_content,
        option_a,
        option_b,
        option_c,
        correct_option,
        answer_explanation
    )
VALUES
    (
        1,
        'What is a variable in programming?',
        'A. A number',
        'B. A container for data',
        'C. A loop statement',
        'B',
        'In programming, a variable is a container for storing data.'
    ),
    (
        2,
        'How many elements are there in the Periodic Table?',
        'A. 92',
        'B. 118',
        'C. 100',
        'B',
        'The Periodic Table currently has 118 known elements.'
    ),
    (
        3,
        'Who painted the Mona Lisa?',
        'A. Vincent van Gogh',
        'B. Leonardo da Vinci',
        'C. Pablo Picasso',
        'B',
        'Leonardo da Vinci painted the Mona Lisa.'
    ),
    (
        4,
        'What is the recommended daily water intake?',
        'A. 2 liters',
        'B. 8 glasses',
        'C. 5 liters',
        'B',
        'The recommended daily water intake is 8 glasses or approximately 2 liters.'
    ),
    (
        5,
        'In which year did World War II end?',
        'A. 1943',
        'B. 1945',
        'C. 1950',
        'B',
        'World War II ended in 1945.'
    );

-- Quiz has questions table
INSERT INTO
    has_questions (question_id, quiz_id, total_questions)
VALUES
    (1, 1, 10),
    (2, 2, 15),
    (3, 3, 12),
    (4, 4, 8),
    (5, 5, 20);

-- Flashcard Sets Table
INSERT INTO
    flashcards (
        flashcard_id,
        question,
        answer,
        answer_explanation
    )
VALUES
    (
        1,
        'What is the capital of France?',
        'Paris',
        'Paris is the capital of France.'
    ),
    (
        2,
        'What is the chemical symbol for gold?',
        'Au',
        'The chemical symbol for gold is Au.'
    ),
    (
        3,
        'Who wrote "Romeo and Juliet"?',
        'William Shakespeare',
        'William Shakespeare wrote "Romeo and Juliet".'
    ),
    (
        4,
        'What is the main component of a balanced diet?',
        'Nutrients',
        'A balanced diet includes a variety of nutrients.'
    ),
    (
        5,
        'Who was the first President of the United States?',
        'George Washington',
        'George Washington was the first President of the United States.'
    );

-- Flashcard content type table
INSERT INTO
    flashcard_content_type (flashcard_id, content_type_id)
VALUES
    (1, 4),
    (2, 4),
    (3, 4),
    (4, 4),
    (5, 4);

-- Quiz taken table
INSERT INTO
    taken (user_id, quiz_id, score, letter_grade)
VALUES
    -- User 1
    (1, 1, 65, 'D'),
    (1, 2, 80, 'B'),
    (1, 3, 75, 'C'),
    (1, 4, 60, 'D'),
    (1, 5, 92, 'A'),
    -- User 2
    (2, 1, 72, 'C'),
    (2, 2, 88, 'B'),
    (2, 3, 80, 'B'),
    (2, 4, 55, 'F'),
    (2, 5, 90, 'A'),
    -- User 3
    (3, 1, 68, 'D'),
    (3, 2, 92, 'A'),
    (3, 3, 78, 'C'),
    (3, 4, 62, 'D'),
    (3, 5, 85, 'B'),
    -- User 4
    (4, 1, 75, 'C'),
    (4, 2, 85, 'B'),
    (4, 3, 72, 'C'),
    (4, 4, 58, 'F'),
    (4, 5, 88, 'B'),
    -- User 5
    (5, 1, 80, 'B'),
    (5, 2, 90, 'A'),
    (5, 3, 82, 'B'),
    (5, 4, 65, 'D'),
    (5, 5, 94, 'A');

-- Referred table
INSERT INTO
    referred (user_id, referred_by)
VALUES
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 2);

-- Admin accounts table
INSERT INTO
    admin_users (
        user_id,
        first_name,
        middle_name,
        last_name,
        email,
        hashed_password,
        join_date,
        joined_time,
        phone,
        admin_code
    )
VALUES
    (
        6,
        'Admin',
        NULL,
        'User',
        'admin@email.com',
        'hashedadminpass',
        '2023-06-01',
        '08:00:00',
        1234567890,
        12345
    );