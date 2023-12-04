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
    (1, 1, 'text'),
    (2, 2, 'video'),
    (3, 3, 'audio'),
    (4, 4, 'text'),
    (5, 5, 'text');

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
    -- Questions 1-10
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
    ),
    (
        6,
        'What is the capital of France?',
        'A. Berlin',
        'B. Madrid',
        'C. Paris',
        'C',
        'Paris is the capital of France.'
    ),
    (
        7,
        'Who wrote "Romeo and Juliet"?',
        'A. Charles Dickens',
        'B. William Shakespeare',
        'C. Jane Austen',
        'B',
        'William Shakespeare wrote "Romeo and Juliet".'
    ),
    (
        8,
        'What is the chemical symbol for gold?',
        'A. Au',
        'B. Fe',
        'C. Ag',
        'A',
        'The chemical symbol for gold is Au.'
    ),
    (
        9,
        'What is the main component of a balanced diet?',
        'A. Carbohydrates',
        'B. Nutrients',
        'C. Proteins',
        'B',
        'A balanced diet includes a variety of nutrients.'
    ),
    (
        10,
        'Who was the first President of the United States?',
        'A. Thomas Jefferson',
        'B. George Washington',
        'C. Abraham Lincoln',
        'B',
        'George Washington was the first President of the United States.'
    ),
    -- Questions 11-20
    (
        11,
        'What is the speed of light?',
        'A. 299,792 km/s',
        'B. 150,000 km/s',
        'C. 500,000 km/s',
        'A',
        'The speed of light in a vacuum is approximately 299,792 kilometers per second.'
    ),
    (
        12,
        'Which planet is known as the Red Planet?',
        'A. Venus',
        'B. Mars',
        'C. Jupiter',
        'B',
        'Mars is known as the Red Planet.'
    ),
    (
        13,
        'Who developed the theory of relativity?',
        'A. Isaac Newton',
        'B. Albert Einstein',
        'C. Galileo Galilei',
        'B',
        'Albert Einstein developed the theory of relativity.'
    ),
    (
        14,
        'What is the largest mammal on Earth?',
        'A. Elephant',
        'B. Blue whale',
        'C. Giraffe',
        'B',
        'The blue whale is the largest mammal on Earth.'
    ),
    (
        15,
        'In which country did the Renaissance begin?',
        'A. Italy',
        'B. France',
        'C. England',
        'A',
        'The Renaissance began in Italy.'
    ),
    (
        16,
        'Who is the author of "To Kill a Mockingbird"?',
        'A. Harper Lee',
        'B. J.K. Rowling',
        'C. Ernest Hemingway',
        'A',
        'Harper Lee wrote "To Kill a Mockingbird".'
    ),
    (
        17,
        'What is the currency of Japan?',
        'A. Won',
        'B. Yen',
        'C. Yuan',
        'B',
        'The currency of Japan is the Yen.'
    ),
    (
        18,
        'What is the capital of Australia?',
        'A. Sydney',
        'B. Melbourne',
        'C. Canberra',
        'C',
        'Canberra is the capital of Australia.'
    ),
    (
        19,
        'Who discovered penicillin?',
        'A. Alexander Fleming',
        'B. Louis Pasteur',
        'C. Marie Curie',
        'A',
        'Alexander Fleming discovered penicillin.'
    ),
    (
        20,
        'What is the chemical symbol for oxygen?',
        'A. O',
        'B. Ox',
        'C. O2',
        'A',
        'The chemical symbol for oxygen is O.'
    ),
    -- Questions 21-30
    (
        21,
        'Who painted "Starry Night"?',
        'A. Pablo Picasso',
        'B. Vincent van Gogh',
        'C. Claude Monet',
        'B',
        'Vincent van Gogh painted "Starry Night".'
    ),
    (
        22,
        'What is the powerhouse of the cell?',
        'A. Nucleus',
        'B. Mitochondria',
        'C. Ribosome',
        'B',
        'Mitochondria are often referred to as the powerhouse of the cell.'
    ),
    (
        23,
        'Which gas do plants absorb during photosynthesis?',
        'A. Oxygen',
        'B. Carbon dioxide',
        'C. Nitrogen',
        'B',
        'Plants absorb carbon dioxide during photosynthesis.'
    ),
    (
        24,
        'Who developed the polio vaccine?',
        'A. Jonas Salk',
        'B. Edward Jenner',
        'C. Albert Sabin',
        'A',
        'Jonas Salk developed the polio vaccine.'
    ),
    (
        25,
        'What is the largest ocean on Earth?',
        'A. Atlantic Ocean',
        'B. Indian Ocean',
        'C. Pacific Ocean',
        'C',
        'The Pacific Ocean is the largest ocean on Earth.'
    ),
    (
        26,
        'What is the square root of 144?',
        'A. 10',
        'B. 12',
        'C. 14',
        'B',
        'The square root of 144 is 12.'
    ),
    (
        27,
        'Who wrote "1984"?',
        'A. George Orwell',
        'B. Aldous Huxley',
        'C. J.K. Rowling',
        'A',
        'George Orwell wrote "1984".'
    ),
    (
        28,
        'What is the process of converting water vapor into liquid water called?',
        'A. Condensation',
        'B. Evaporation',
        'C. Precipitation',
        'A',
        'The process of converting water vapor into liquid water is called condensation.'
    ),
    (
        29,
        'Which planet is known as the "Red Planet"?',
        'A. Venus',
        'B. Mars',
        'C. Jupiter',
        'B',
        'Mars is known as the "Red Planet".'
    ),
    (
        30,
        'Who is known as the "Father of Computer Science"?',
        'A. Alan Turing',
        'B. Bill Gates',
        'C. Steve Jobs',
        'A',
        'Alan Turing is known as the "Father of Computer Science".'
    ),
    -- Questions 31-40
    (
        31,
        'What is the capital of Brazil?',
        'A. Rio de Janeiro',
        'B. Brasília',
        'C. São Paulo',
        'B',
        'Brasília is the capital of Brazil.'
    ),
    (
        32,
        'Who wrote "Pride and Prejudice"?',
        'A. Jane Austen',
        'B. Charlotte Brontë',
        'C. Emily Brontë',
        'A',
        'Jane Austen wrote "Pride and Prejudice".'
    ),
    (
        33,
        'What is the largest desert in the world?',
        'A. Sahara Desert',
        'B. Gobi Desert',
        'C. Antarctica',
        'C',
        'Antarctica is the largest desert in the world.'
    ),
    (
        34,
        'Who developed the theory of evolution by natural selection?',
        'A. Charles Darwin',
        'B. Gregor Mendel',
        'C. Alfred Russel Wallace',
        'A',
        'Charles Darwin developed the theory of evolution by natural selection.'
    ),
    (
        35,
        'What is the capital of China?',
        'A. Beijing',
        'B. Shanghai',
        'C. Hong Kong',
        'A',
        'Beijing is the capital of China.'
    ),
    (
        36,
        'What is the chemical symbol for sodium?',
        'A. S',
        'B. Na',
        'C. So',
        'B',
        'The chemical symbol for sodium is Na.'
    ),
    (
        37,
        'Who is the Greek god of the sea?',
        'A. Zeus',
        'B. Poseidon',
        'C. Hades',
        'B',
        'Poseidon is the Greek god of the sea.'
    ),
    (
        38,
        'What is the smallest prime number?',
        'A. 0',
        'B. 1',
        'C. 2',
        'C',
        'The smallest prime number is 2.'
    ),
    (
        39,
        'Who painted the Sistine Chapel ceiling?',
        'A. Leonardo da Vinci',
        'B. Michelangelo',
        'C. Raphael',
        'B',
        'Michelangelo painted the Sistine Chapel ceiling.'
    ),
    (
        40,
        'What is the capital of India?',
        'A. Mumbai',
        'B. New Delhi',
        'C. Kolkata',
        'B',
        'New Delhi is the capital of India.'
    ),
    -- Questions 41-50
    (
        41,
        'Who is the author of "The Great Gatsby"?',
        'A. F. Scott Fitzgerald',
        'B. Ernest Hemingway',
        'C. Jane Austen',
        'A',
        'F. Scott Fitzgerald wrote "The Great Gatsby".'
    ),
    (
        42,
        'What is the largest organ in the human body?',
        'A. Heart',
        'B. Liver',
        'C. Skin',
        'C',
        'The largest organ in the human body is the skin.'
    ),
    (
        43,
        'Who was the first woman to win a Nobel Prize?',
        'A. Marie Curie',
        'B. Rosalind Franklin',
        'C. Dorothy Crowfoot Hodgkin',
        'A',
        'Marie Curie was the first woman to win a Nobel Prize.'
    ),
    (
        44,
        'What is the currency of Germany?',
        'A. Franc',
        'B. Mark',
        'C. Euro',
        'C',
        'The currency of Germany is the Euro.'
    ),
    (
        45,
        'In which year did the Titanic sink?',
        'A. 1912',
        'B. 1915',
        'C. 1918',
        'A',
        'The Titanic sank in 1912.'
    ),
    (
        46,
        'Who discovered electricity?',
        'A. Thomas Edison',
        'B. Benjamin Franklin',
        'C. Nikola Tesla',
        'B',
        'Benjamin Franklin is often credited with discovering electricity.'
    ),
    (
        47,
        'What is the square of 9?',
        'A. 81',
        'B. 72',
        'C. 64',
        'A',
        'The square of 9 is 81.'
    ),
    (
        48,
        'Who wrote "The Catcher in the Rye"?',
        'A. J.D. Salinger',
        'B. Mark Twain',
        'C. Ernest Hemingway',
        'A',
        'J.D. Salinger wrote "The Catcher in the Rye".'
    ),
    (
        49,
        'What is the largest moon of Saturn?',
        'A. Titan',
        'B. Enceladus',
        'C. Europa',
        'A',
        'Titan is the largest moon of Saturn.'
    ),
    (
        50,
        'Who is the founder of Microsoft?',
        'A. Bill Gates',
        'B. Steve Jobs',
        'C. Mark Zuckerberg',
        'A',
        'Bill Gates is the founder of Microsoft.'
    );

-- Quiz has questions table
INSERT INTO
    has_questions (question_id, quiz_id, total_questions)
VALUES
    --Quiz 1
    (1, 1, 10),
    (2, 1, 10),
    (3, 1, 10),
    (4, 1, 10),
    (5, 1, 10),
    (6, 1, 10),
    (7, 1, 10),
    (8, 1, 10),
    (9, 1, 10),
    (10, 1, 10),
    --Quiz 2
    (1, 2, 10),
    (2, 2, 10),
    (3, 2, 10),
    (4, 2, 10),
    (5, 2, 10),
    (6, 2, 10),
    (7, 2, 10),
    (8, 2, 10),
    (9, 2, 10),
    (10, 2, 10),
    --Quiz 3
    (1, 3, 10),
    (2, 3, 10),
    (3, 3, 10),
    (4, 3, 10),
    (5, 3, 10),
    (6, 3, 10),
    (7, 3, 10),
    (8, 3, 10),
    (9, 3, 10),
    (10, 3, 10),
    --Quiz 4
    (1, 4, 10),
    (2, 4, 10),
    (3, 4, 10),
    (4, 4, 10),
    (5, 4, 10),
    (6, 4, 10),
    (7, 4, 10),
    (8, 4, 10),
    (9, 4, 10),
    (10, 4, 10),
    --Quiz 5
    (1, 5, 10),
    (2, 5, 10),
    (3, 5, 10),
    (4, 5, 10),
    (5, 5, 10),
    (6, 5, 10),
    (7, 5, 10),
    (8, 5, 10),
    (9, 5, 10),
    (10, 5, 10);

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
    (5, 3);

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