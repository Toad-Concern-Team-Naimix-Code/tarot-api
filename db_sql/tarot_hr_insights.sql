CREATE TABLE IF NOT EXISTS tarot_hr_insights (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT NOT NULL,
    workplace_relationship_interpretation TEXT NOT NULL,
    career_interpretation TEXT NOT NULL
);

INSERT INTO tarot_hr_insights (name, description, workplace_relationship_interpretation, career_interpretation) VALUES
('Шут',
'Шут — тот ещё авантюрист! Он радостно бросается в новые начинания и никогда не знает, что ждёт за углом. Этот кандидат готов рискнуть и, возможно, устроить небольшое веселье.',
'На работе Шут всегда будет вдохновлять коллег своей свежестью и спонтанностью. Правда, иногда коллеги будут чувствовать себя, как в кругосветном турне с открытым финалом!',
'Шут отлично подойдёт для стартапов и динамичных позиций. Если надо рискнуть и привнести свежие идеи, это точно он! Но не рассчитывай, что он будет сидеть на одном месте слишком долго.'),

('Маг',
'Маг — мастер своего дела. Он не просто профессионал, он настоящий волшебник! Знает, как достичь цели и использует все доступные ресурсы.',
'Маг умеет расположить к себе и блестяще использует свои связи. С ним даже самые трудные задачи становятся выполнимыми, а коллеги идут за ним, как за путеводной звездой.',
'На новой должности Маг быстро вникнет в суть и станет двигателем перемен. Это ваш идеальный кандидат для амбициозных проектов и роста компании.'),

('Жрица',
'Жрица — мудрая и спокойная, она полагается на свою интуицию. Этот кандидат отлично чувствует коллектив и может предугадывать, как улучшить атмосферу на рабочем месте.',
'В коллективе Жрица создаёт атмосферу доверия и открытости. Она предпочитает не сплетничать, а слушать и понимать – и коллеги это очень ценят.',
'На карьере Жрица не торопится к вершинам, но её можно доверить самые сложные задачи. В должности аналитика или стратега она незаменима.'),

('Императрица',
'Императрица — заботливая и щедрая натура. Она привносит в рабочую жизнь тепло и гармонию.',
'Коллеги к ней тянутся как к магниту: Императрица умеет создать атмосферу уюта и поддержки. На её месте отдыхают даже самые тревожные сотрудники.',
'В карьере Императрица отлично справляется с ролью тимлида или HR. Она видит таланты других и помогает им раскрыться.'),

('Император',
'Император – властный и надёжный. Этот кандидат точно не пропустит дедлайн и будет следовать правилам до последней буквы.',
'Император задаёт тон и может навести порядок даже в хаотичной команде. Он создаёт ощущение стабильности и чёткой структуры.',
'Если нужен лидер с хорошей выносливостью, Император станет отличным выбором. Под его управлением компания будет процветать.'),

('Жрец',
'Жрец – духовный наставник и мудрый советчик. Этот кандидат привнесёт в коллектив спокойствие и поддержку.',
'На рабочем месте Жрец – тот самый коллега, к которому приходят за советом. Он искренне помогает и не боится делиться знаниями.',
'Жрец подойдёт для образовательных ролей или наставничества. Он видит потенциал в других и готов его раскрыть.'),

('Влюбленные',
'Влюбленные – это карта выбора и гармонии. Этот кандидат способен находить баланс и гармонизировать коллектив.',
'На работе Влюбленные напоминают всем, что важна командная работа. Они становятся «мостиком» между коллегами и способствуют позитивной атмосфере.',
'В карьере Влюбленные помогают принимать важные решения. Идеально подходит для роли HR, наставника или тимлида.'),

('Колесница',
'Колесница – воплощение целеустремлённости и напора. Этот кандидат умеет двигаться вперёд и не боится трудностей.',
'На работе Колесница заряжает команду энергией и мотивирует на достижение целей. Иногда коллеги могут считать его слишком напористым, но результат всегда того стоит.',
'Колесница подойдёт для управленческой позиции или проекта, где важно «пробить стену» и идти к успеху.'),

('Сила',
'Сила – внутренний стержень и мягкость одновременно. Этот кандидат стойкий, но гибкий, как бамбук.',
'Сила в коллективе умеет поддерживать гармонию и помогает справляться с конфликтами. Коллеги чувствуют рядом с ним уверенность.',
'Для ответственной должности или работы с клиентами это идеальный выбор. Он стойко выдержит все трудности.'),

('Отшельник',
'Отшельник – спокойный и вдумчивый. Он погружается в анализ и всегда найдёт нестандартное решение.',
'Отшельник может показаться замкнутым, но в трудные моменты коллеги понимают: он всегда готов дать мудрый совет.',
'На работе Отшельник предпочитает аналитические или исследовательские задачи, где он может углубиться в детали.'),

('Фортуна',
'Фортуна – символ удачи и перемен. Этот кандидат – настоящая находка, и с ним в команде явно не заскучаешь!',
'Фортуна приносит дух перемен. Если что-то не получается, этот кандидат всегда найдёт выход и вдохновит остальных.',
'Фортуна идеально подойдёт для динамичных проектов, где требуется гибкость и способность быстро адаптироваться.'),

('Справедливость',
'Справедливость – это принцип и честность. Этот кандидат строго следует правилам, но всегда справедлив к коллегам.',
'Справедливость создаёт атмосферу, где царят уважение и честность. Коллеги знают, что могут на него положиться.',
'Для юридической должности, аудита или контроля качества Справедливость – идеальный кандидат.'),

('Повешенный',
'Повешенный — тот, кто не боится посмотреть на вещи под новым углом. Готов к нестандартным решениям.',
'В коллективе Повешенный помогает находить неожиданные подходы. Он немного медлителен, но всегда видит то, что ускользает от других.',
'Этот кандидат подходит для креативных должностей или проектного анализа.'),

('Смерть',
'Смерть – это не конец, а трансформация. Этот кандидат способен полностью изменить ход дела.',
'Смерть в коллективе — мастер реорганизации. Он уберёт всё лишнее и даст команде шанс начать с нуля.',
'Этот кандидат идеально подходит для реструктуризации компании или проектного обновления.'),

('Умеренность',
'Умеренность — символ баланса. Этот кандидат не торопится, но всегда достигает результата.',
'В коллективе Умеренность создаёт спокойную атмосферу, уравновешивает конфликты и поддерживает стабильность.',
'Для проектов, где важен долгий и стабильный рост, Умеренность станет надёжным выбором.'),

('Дьявол',
'Дьявол — это карта искушения и энергии. Этот кандидат знает, как сделать работу интереснее.',
'Коллеги любят Дьявола за его юмор и лёгкость, но он может привнести и немного хаоса!',
'Дьявол подойдёт для креативной сферы, где нужно иногда нарушать правила и находить нестандартные решения.'),

('Башня',
'Башня — символ резких перемен. Этот кандидат любит разрушать старое и создавать новое.',
'Коллеги могут сначала бояться Башню, но потом понимают, что изменения были к лучшему.',
'Башня идеально подходит для стартапов или реструктуризаций, где старое нужно заменить новым.'),

('Звезда',
'Звезда — вдохновение и надежда. Этот кандидат приносит свет и помогает коллегам верить в успех.',
'В коллективе Звезда становится примером. Она мотивирует коллег двигаться к общей цели.',
'Звезда отлично подойдёт для ролей наставника или лидера, который вдохновляет и помогает достигать.'),

('Луна',
'Луна — интуитивная и немного загадочная. Этот кандидат видит скрытые аспекты ситуации и всегда находит путь туда, где другие не видят выхода.', 'Луна в коллективе – это кто-то, кто видит проблемы с другого угла. Она часто предсказывает проблемы до того, как они возникнут.', 'Луна подходит для аналитиков или тех, кто работает в условиях неопределенности и изменения.'),

('Солнце', 'Солнце — символ успеха и оптимизма. Этот кандидат всегда с улыбкой на лице и светит всем вокруг.', 'Солнце приносит радость в коллектив и помогает справиться с трудностями с улыбкой.', 'Если нужна энергия и драйв для компании, Солнце идеально подойдёт для активной роли в коллективе.'),

('Суд', 'Суд — это подведение итогов. Этот кандидат умеет объективно оценивать ситуацию и принимать правильные решения.', 'В коллективе Суд помогает разобраться в сложных вопросах и подвести итоги.', 'Суд подойдёт для роли оценки результатов или руководителя проекта, который умеет завершить начатое.'),

('Мир', 'Мир — это успех и завершение. Этот кандидат может гордиться своим вкладом и успехами.', 'В коллективе Мир – это стабильность и поддержка. Он завершает проекты на высшем уровне.', 'Для высших должностей или завершения больших проектов, Мир будет настоящим мастером.');

SELECT * FROM tarot_hr_insights;
