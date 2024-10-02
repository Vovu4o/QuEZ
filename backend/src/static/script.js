function showPage(page) {
    // Убираем активность с текущих страниц
    document.querySelectorAll('.page').forEach(page => page.classList.remove('active'));
    document.querySelectorAll('.cloud').forEach(cloud => cloud.classList.remove('active'));

    // Показ выбранной страницы
    document.getElementById(page).classList.add('active');
    document.getElementById(page + '-btn').classList.add('active');
}

function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    const wordList = document.getElementById('wordList');

    if (fileInput.files.length > 0) {
        const file = fileInput.files[0];
        const reader = new FileReader();
        
        reader.onload = function(event) {
            try {
                const data = JSON.parse(event.target.result);
                wordList.textContent = JSON.stringify(data, null, 2);
            } catch (error) {
                wordList.textContent = 'Ошибка чтения файла!';
            }
        };
        
        reader.readAsText(file);
    } else {
        wordList.textContent = 'Пожалуйста, выберите файл!';
    }
}
