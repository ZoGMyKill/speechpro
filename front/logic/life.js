let currentUser = null;

function toggleLoginForm(e) {
    e.preventDefault();
    const form = document.querySelector('.modal-form');
    const heading = document.querySelector('.modal h2');

    if (form.id === 'loginForm') {
        heading.textContent = 'Добро пожаловать в SpeechPro';
        form.id = 'registerForm';
        form.innerHTML = `
            <input type="text" name="fullName" placeholder="Полное Имя" required>
            <input type="email" name="email" placeholder="Электронная почта" required>
            <input type="password" name="password" placeholder="Пароль" required>
            <input type="password" name="confirmPassword" placeholder="Повторите Пароль" required>
            <button type="submit" class="btn">Зарегистрироваться</button>
            <p style="text-align: center; margin: 10px 0;">
                Уже есть аккаунт? <a href="#" onclick="toggleLoginForm(event)" style="color: #3498db;">Войти</a>
            </p>
        `;
    } else {
        heading.textContent = 'Войти в SpeechPro';
        form.id = 'loginForm';
        form.innerHTML = `
            <input type="email" name="email" placeholder="Электронная почта" required>
            <input type="password" name="password" placeholder="Пароль" required>
            <button type="submit" class="btn">Войти</button>
            <p style="text-align: center; margin: 10px 0;">
                Нет аккаунта? <a href="#" onclick="toggleLoginForm(event)" style="color: #3498db;">Зарегистрироваться</a>
            </p>
        `;
    }
}

document.querySelectorAll('.modal-form').forEach(form => {
    form.addEventListener('submit', function(e) {
        e.preventDefault();

        const formData = new FormData(form);
        const userData = {};
        formData.forEach((value, key) => userData[key] = value);

        if (form.id === 'registerForm') {
            currentUser = {
                name: userData['fullName'],
                email: userData['email'],
                membership: 'Премиум',
                speechesAnalyzed: 0
            };
        } else {
            currentUser = {
                name: userData['email'].split('@')[0],
                email: userData['email'],
                membership: 'Премиум',
                speechesAnalyzed: 15
            };
        }

        updateAccountInfo();
        document.getElementById('registerModal').style.display = 'none';
    });
});

function updateAccountInfo() {
    if (currentUser) {
        const accountInfo = document.getElementById('account-info');
        accountInfo.innerHTML = `
            <h2>Личный кабинет</h2>
            <ul>
                <li><strong>Имя:</strong> ${currentUser.name}</li>
                <li><strong>Электронная почта:</strong> ${currentUser.email}</li>
                <li><strong>Подписка:</strong> ${currentUser.membership}</li>
                <li><strong>Всего проведённых анализов:</strong> ${currentUser.speechesAnalyzed}</li>
            </ul>
            <button class="btn" onclick="logOut()">Выйти из аккаунта</button>
        `;
    }
}

function closeModal() {
    document.getElementById('registerModal').style.display = 'none';
}

window.onclick = function(event) {
    const modal = document.getElementById('registerModal');
    if (event.target === modal) {
        modal.style.display = 'none';
    }
};

window.onload = function() {
    document.querySelectorAll('.side-menu button').forEach(btn => btn.classList.remove('active'));
    document.querySelector('.side-menu button[title="Загрузить Видео"]').classList.add('active');
    document.getElementById('registerModal').style.display = 'flex';

    const form = document.querySelector('.modal-form');
    const heading = document.querySelector('.modal h2');
    heading.textContent = 'Войти в SpeechPro';
    form.id = 'loginForm';
    form.innerHTML = `
        <input type="email" name="email" placeholder="Электронная почта" required>
        <input type="password" name="password" placeholder="Пароль" required>
        <button type="submit" class="btn">Войти</button>
        <p style="text-align: center; margin: 10px 0;">
            Нет аккаунта? <a href="#" onclick="toggleLoginForm(event)" style="color: #3498db;">Зарегистрироваться</a>
        </p>
    `;
};

function hideAllContent() {
    document.querySelector('.main-content').style.display = 'none';
    let homeContent = document.getElementById('home-page');
    if (homeContent) {
        homeContent.remove();
    }
    document.getElementById('transcript-history').style.display = 'none';
    document.getElementById('account-info').style.display = 'none';
    document.getElementById('share-page').style.display = 'none';
}

let deleteConfirmState = false;

document.getElementById('video-upload').addEventListener('change', function(event) {
    let file = event.target.files[0];
    if (file) {
        let blobURL = URL.createObjectURL(file);
        document.querySelector('#video-player video').src = blobURL;
        document.getElementById('deleteBtn').style.display = 'inline-block';
        document.getElementById('decryptBtn').style.display = 'inline-block';
        document.getElementById('copyBtn').style.display = 'none';
        resetButtonStates();
        setTimeout(analyzeVideo, 2000);
        event.target.value = '';
    }
});

function analyzeVideo() {
    let transcript = "Привет всем, эм, сегодня я собираюсь поговорить о, знаешь, важности публичных выступлений. Как бы, это навык, который может действительно, ээ, улучшить вашу карьеру и личную жизнь.";
    transcript = transcript.replace(/\b(эм|ээ|как бы|знаешь)\b/gi, '<span class="filler-word">$1</span>');
    document.getElementById('transcript').innerHTML = `<h3>Анализ выступления:</h3><p>${transcript}</p>`;

    let analysisResults = [
        "В результате - 5",
        "Он - 6",
        "Вас - 2"
    ];

    let keywordResults = [
        "Речь",
        "Развитие",
        "Выступление",
        "Мастерство"
    ];

    let weakWordResults = [
        "Может быть",
        "Как бы",
        "Типа",
        "Просто"
    ];

    let analysisList = document.getElementById('analysis-list');
    analysisList.innerHTML = '';
    analysisResults.forEach(result => {
        let li = document.createElement('li');
        li.textContent = result;
        analysisList.appendChild(li);
    });

    let analysisCard = document.getElementById('analysis-card');
    let tipsCard = document.getElementById('tips-card');

    let weakWordsCard = document.getElementById('weak-words-card');
    if (!weakWordsCard) {
        weakWordsCard = document.createElement('div');
        weakWordsCard.id = 'weak-words-card';
        weakWordsCard.className = 'analysis-card collapsible';
        weakWordsCard.innerHTML = `
            <h3>Слабые Слова</h3>
            <ul id="weak-words-list"></ul>
        `;
        let improvementsCard = document.getElementById('improvements-card');
        improvementsCard.parentNode.insertBefore(weakWordsCard, improvementsCard);
    }

    let tipsList = document.getElementById('tips-list');
    tipsList.innerHTML = '';
    keywordResults.forEach(keyword => {
        let li = document.createElement('li');
        li.textContent = keyword;
        tipsList.appendChild(li);
    });

    let weakWordsList = document.getElementById('weak-words-list');
    weakWordsList.innerHTML = '';
    weakWordResults.forEach(word => {
        let li = document.createElement('li');
        li.textContent = word;
        weakWordsList.appendChild(li);
    });

    document.getElementById('transcript').style.maxHeight = document.getElementById('transcript').scrollHeight + "px";
    document.getElementById('analysis-card').style.maxHeight = document.getElementById('analysis-card').scrollHeight + "px";
    document.getElementById('tips-card').style.maxHeight = document.getElementById('tips-card').scrollHeight + "px";
    document.getElementById('weak-words-card').style.maxHeight = document.getElementById('weak-words-card').scrollHeight + "px";
    document.getElementById('improvements-card').style.maxHeight = document.getElementById('improvements-card').scrollHeight + "px";

    document.getElementById('copyBtn').style.display = 'inline-block';
}

function copyTranscript() {
    let tempInput = document.createElement('textarea');
    tempInput.value = document.getElementById('transcript').innerText.replace('Субтитры:', '').trim();
    document.body.appendChild(tempInput);
    tempInput.select();
    document.execCommand('copy');
    document.body.removeChild(tempInput);
    alert('Субтитры скопирован в буфер обмена!');
}

document.querySelector('.account-btn').addEventListener('click', function() {
    showAccountInfo();
});

document.getElementById('deleteBtn').addEventListener('click', function() {
    if (!deleteConfirmState) {
        this.textContent = 'Вы уверены?';
        deleteConfirmState = true;
    } else {
        resetToInitialState();
    }
});

document.getElementById('decryptBtn').addEventListener('click', function() {
    console.log('Инициализация расшифровки видео.');
    setTimeout(() => {
        console.log('Видео успешно расшифровано!');
    }, 2000);
});

function resetButtonStates() {
    document.getElementById('deleteBtn').textContent = 'Удалить Видео';
    deleteConfirmState = false;
}

function resetToInitialState() {
    const videoElement = document.querySelector('#video-player video');
    if (videoElement.src) {
        URL.revokeObjectURL(videoElement.src);
    }
    videoElement.src = '';
    document.getElementById('deleteBtn').style.display = 'none';
    document.getElementById('decryptBtn').style.display = 'none';
    document.getElementById('copyBtn').style.display = 'none';
    resetButtonStates();
    collapseAllSections();
    document.getElementById('analysis-list').innerHTML = '';
    document.getElementById('tips-list').innerHTML = '';
    document.getElementById('weak-words-list').innerHTML = '';
    document.getElementById('transcript').innerHTML = '';
    document.getElementById('video-upload').value = '';
}

function collapseAllSections() {
    document.getElementById('transcript').style.maxHeight = null;
    document.getElementById('analysis-card').style.maxHeight = null;
    document.getElementById('tips-card').style.maxHeight = null;
    document.getElementById('weak-words-card').style.maxHeight = null;
    document.getElementById('improvements-card').style.maxHeight = null;
}

function setActivePage(button) {
    document.querySelectorAll('.side-menu button').forEach(btn => btn.classList.remove('active'));
    button.classList.add('active');
}

function showHomePage() {
    let homeContent = `
        <div id="home-page" class="home-content">
            <h3>Добро пожаловать в SpeachPro</h3>
            <p>SpeachPro - это инструмент на основе ИИ, предназначенный для улучшения ваших навыков публичных выступлений. С нашей продвинутой системой анализа и обратной связи вы можете улучшить подачу речи, сократить использование паразитных слов и укрепить свою уверенность.</p>
            <h2>Ключевые Функции:</h2>
            <ul>
                <li>Загрузите и проанализируйте свои видео выступления</li>
                <li>Получите мгновенную обратную связь о своих речевых паттернах</li>
                <li>Получите персонализированные советы по улучшению</li>
                <li>Отслеживайте свой прогресс с течением времени</li>
                <li>Безопасное хранение видео с опциями шифрования</li>
            </ul>
            <p>Начните свой путь к тому, чтобы стать лучшим оратором сегодня с SpeachPro!</p>
        </div>
    `;
    document.querySelector('header').insertAdjacentHTML('afterend', homeContent);
}

function showTranscriptHistory() {
    document.getElementById('transcript-history').style.display = 'block';
}

function viewTranscript(id) {
    alert(`Просмотр транскрипта ${id}. Эта функция скоро появится!`);
}

function showAccountInfo() {
    hideAllContent();
    document.getElementById('account-info').style.display = 'block';
}

function logOut() {
    currentUser = null;
    updateAccountInfo();
    document.getElementById('registerModal').style.display = 'flex';
}

function showSharePage() {
    hideAllContent();
    document.getElementById('share-page').style.display = 'block';
    document.getElementById('share-url').value = window.location.href;
}

document.querySelectorAll('.side-menu button').forEach(button => {
    button.addEventListener('click', function() {
        setActivePage(this);
        hideAllContent();
        if (this.title === 'Главная') {
            showHomePage();
        } else if (this.title === 'История Транскриптов') {
            showTranscriptHistory();
        } else if (this.title === 'Общий Доступ') {
            showSharePage();
        } else {
            document.querySelector('.main-content').style.display = 'flex';
        }
    });
});

function shareOnFacebook() {
    const url = encodeURIComponent(window.location.href);
    const facebookShareURL = `https://www.facebook.com/sharer/sharer.php?u=${url}`;
    window.open(facebookShareURL, '_blank', 'width=600,height=400');
}

function shareOnTwitter() {
    const text = encodeURIComponent("Проверьте SpeachPro, чтобы улучшить свои навыки публичных выступлений!");
    const url = encodeURIComponent(window.location.href);
    const twitterShareURL = `https://twitter.com/intent/tweet?text=${text}&url=${url}`;
    window.open(twitterShareURL, '_blank', 'width=600,height=400');
}

function shareOnLinkedIn() {
    const url = encodeURIComponent(window.location.href);
    const linkedinShareURL = `https://www.linkedin.com/sharing/share-offsite/?url=${url}`;
    window.open(linkedinShareURL, '_blank', 'width=600,height=400');
}

function copyShareLink() {
    const shareUrl = document.getElementById('share-url');
    shareUrl.select();
    shareUrl.setSelectionRange(0, 99999);
    document.execCommand('copy');
    alert('Ссылка на общий доступ скопирована в буфер обмена!');
}

function toggleList(listId) {
    const listContent = document.getElementById(`${listId}-list`);
    const button = listContent.previousElementSibling.querySelector('.collapse-btn');

    if (listContent.classList.contains('expanded')) {
        listContent.classList.remove('expanded');
        button.classList.add('collapsed');
    } else {
        listContent.classList.add('expanded');
        button.classList.remove('collapsed');
    }
}