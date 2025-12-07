// 검색 기능
function performSearch() {
    const query = document.getElementById('searchInput').value.trim();
    const resultsDiv = document.getElementById('searchResults');
    
    if (query === '') {
        resultsDiv.classList.remove('active');
        return;
    }
    
    fetch(`/api/search?q=${encodeURIComponent(query)}`)
        .then(response => response.json())
        .then(data => {
            resultsDiv.innerHTML = '';
            
            if (data.length === 0) {
                resultsDiv.innerHTML = '<p>검색 결과가 없습니다.</p>';
                resultsDiv.classList.add('active');
                return;
            }
            
            data.forEach(item => {
                const resultItem = document.createElement('div');
                resultItem.className = 'search-result-item';
                
                let badges = '';
                if (item.has_image) badges += '<span class="badge badge-image">📷 이미지</span>';
                if (item.has_video) badges += '<span class="badge badge-video">🎥 동영상</span>';
                if (item.has_code) badges += '<span class="badge badge-code">💻 코드</span>';
                
                resultItem.innerHTML = `
                    <h3><a href="/formula/${item.id}">${item.name}</a></h3>
                    ${badges ? `<div class="media-badges">${badges}</div>` : ''}
                    <p><strong>카테고리:</strong> ${item.category}</p>
                    <p>${item.description}</p>
                `;
                resultsDiv.appendChild(resultItem);
            });
            
            resultsDiv.classList.add('active');
        })
        .catch(error => {
            console.error('검색 오류:', error);
            resultsDiv.innerHTML = '<p>검색 중 오류가 발생했습니다.</p>';
            resultsDiv.classList.add('active');
        });
}

// Enter 키로 검색
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    if (searchInput) {
        searchInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                performSearch();
            }
        });
    }
});

