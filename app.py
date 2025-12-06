from flask import Flask, render_template, jsonify, request
import json
import os

app = Flask(__name__)

# 수학 공식 데이터 로드
def load_formulas():
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'formulas.json')
    if os.path.exists(data_path):
        with open(data_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"categories": []}

# 메인 페이지
@app.route('/')
def index():
    return render_template('index.html')

# 공식 목록 페이지
@app.route('/formulas')
def formulas():
    data = load_formulas()
    category = request.args.get('category', 'all')
    
    if category == 'all':
        formulas_list = []
        for cat in data.get('categories', []):
            formulas_list.extend(cat.get('formulas', []))
    else:
        formulas_list = []
        for cat in data.get('categories', []):
            if cat.get('id') == category:
                formulas_list = cat.get('formulas', [])
                break
    
    return render_template('formulas.html', 
                         formulas=formulas_list, 
                         categories=data.get('categories', []),
                         current_category=category)

# 공식 상세 페이지
@app.route('/formula/<int:formula_id>')
def formula_detail(formula_id):
    data = load_formulas()
    for cat in data.get('categories', []):
        for formula in cat.get('formulas', []):
            if formula.get('id') == formula_id:
                return render_template('formula_detail.html', 
                                     formula=formula,
                                     category=cat)
    return "공식을 찾을 수 없습니다.", 404

# 검색 API
@app.route('/api/search')
def search():
    query = request.args.get('q', '').lower()
    data = load_formulas()
    results = []
    
    for cat in data.get('categories', []):
        for formula in cat.get('formulas', []):
            if (query in formula.get('name', '').lower() or 
                query in formula.get('description', '').lower()):
                results.append({
                    'id': formula.get('id'),
                    'name': formula.get('name'),
                    'category': cat.get('name'),
                    'description': formula.get('description', '')[:100] + '...',
                    'has_image': bool(formula.get('image')),
                    'has_video': bool(formula.get('video')),
                    'has_code': bool(formula.get('code'))
                })
    
    return jsonify(results)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug, host='0.0.0.0', port=port)

