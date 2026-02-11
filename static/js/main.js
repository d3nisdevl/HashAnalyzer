document.addEventListener('DOMContentLoaded', function() {
    const hashInput = document.getElementById('hash-input');
    const analyzeBtn = document.getElementById('analyze-btn');
    const spinner = document.getElementById('spinner');
    const btnText = document.getElementById('btn-text');
    const result = document.getElementById('result');
    const resultIcon = document.getElementById('result-icon');
    const resultTitle = document.getElementById('result-title');
    const resultDetails = document.getElementById('result-details');
    const errorMessage = document.getElementById('error-message');
    
    hashInput.focus();
    
    analyzeBtn.addEventListener('click', analyzeHash);
    

    hashInput.addEventListener('keyup', function(event) {
        if (event.key === 'Enter') {
            analyzeHash();
        }
    });
    

    function analyzeHash() {
        const hash = hashInput.value.trim();
        
        if (!hash) {
            showError('Пожалуйста, введите хеш для анализа!');
            return;
        }
        
        hideError();
        hideResult();
        setLoading(true);
        
        fetch(`/api/detect?hash_str=${encodeURIComponent(hash)}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`Ошибка сервера: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                displayResult(data);
                setLoading(false);
            })
            .catch(error => {
                console.error('Ошибка:', error);
                showError(`Не удалось проанализировать хеш: ${error.message}`);
                setLoading(false);
            });
    }
    

    function setLoading(isLoading) {
        if (isLoading) {
            spinner.style.display = 'inline-block';
            btnText.textContent = 'Анализ...';
            analyzeBtn.disabled = true;
        } else {
            spinner.style.display = 'none';
            btnText.textContent = 'Анализировать Хеш';
            analyzeBtn.disabled = false;
        }
    }
    

    function displayResult(data) {
        if (data.type === 'UNKNOWN') {
            resultIcon.className = 'result-icon unknown';
            resultIcon.textContent = '?';
            resultTitle.textContent = 'Неизвестный тип хеша';
        } else {
            resultIcon.className = 'result-icon identified';
            resultIcon.textContent = '✓';
            resultTitle.textContent = `Определен как ${data.type}`;
        }
        
        let detailsHTML = '';
        
        detailsHTML += `
            <div class="detail-item">
                <div class="detail-label">Type</div>
                <div class="detail-value">${escapeHtml(data.type)}</div>
            </div>
        `;
        
        detailsHTML += `
            <div class="detail-item">
                <div class="detail-label">Length</div>
                <div class="detail-value">${escapeHtml(data.length.toString())} chars</div>
            </div>
        `;
        
        detailsHTML += `
            <div class="detail-item">
                <div class="detail-label">Hashcat</div>
                <div class="detail-value">${escapeHtml(data.hashcat)}</div>
            </div>
        `;
        
        resultDetails.innerHTML = detailsHTML;
        
        result.classList.add('active');
    }
    

    function hideResult() {
        result.classList.remove('active');
    }
    

    function showError(message) {
        errorMessage.textContent = message;
        errorMessage.classList.add('active');
    }
    

    function hideError() {
        errorMessage.classList.remove('active');
    }
    

    function escapeHtml(unsafe) {
        return unsafe
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#039;");
    }
    
    
    setTimeout(() => {
        document.querySelector('header').style.opacity = '1';
        document.querySelector('header').style.transform = 'translateY(0)';
    }, 100);
});