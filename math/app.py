from flask import Flask, render_template, jsonify, request, send_from_directory
import json
import os
from werkzeug.utils import secure_filename
import uuid

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'static', 'images')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# 허용된 파일 확장자
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

# 수학 공식 데이터 로드
def load_formulas():
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'formulas.json')
    if os.path.exists(data_path):
        with open(data_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"categories": []}

# 수학 공식 데이터 저장
def save_formulas(data):
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'formulas.json')
    with open(data_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# 허용된 파일 확장자 확인
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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

# 이미지 관리 페이지
@app.route('/admin/images')
def admin_images():
    return render_template('admin_images.html')

# 이미지 목록 조회 API
@app.route('/api/images')
def list_images():
    images_dir = app.config['UPLOAD_FOLDER']
    images = []
    if os.path.exists(images_dir):
        for filename in os.listdir(images_dir):
            if allowed_file(filename):
                images.append({
                    'filename': filename,
                    'url': f'/static/images/{filename}'
                })
    return jsonify(images)

# 이미지 업로드 API
@app.route('/api/upload-image', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': '파일이 없습니다.'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': '파일이 선택되지 않았습니다.'}), 400
    
    if file and allowed_file(file.filename):
        # 파일명 보안 처리 및 고유 ID 추가
        original_filename = secure_filename(file.filename)
        filename, ext = os.path.splitext(original_filename)
        unique_filename = f"{filename}_{uuid.uuid4().hex[:8]}{ext}"
        
        # 업로드 폴더가 없으면 생성
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        
        # 파일 저장
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(filepath)
        
        return jsonify({
            'success': True,
            'filename': unique_filename,
            'url': f'/static/images/{unique_filename}'
        })
    
    return jsonify({'error': '허용되지 않은 파일 형식입니다.'}), 400

# 공식의 이미지 경로 업데이트 API
@app.route('/api/formula/<int:formula_id>/image', methods=['PUT'])
def update_formula_image(formula_id):
    data = request.get_json()
    image_path = data.get('image_path', '')
    
    formulas_data = load_formulas()
    
    # 공식 찾기 및 이미지 경로 업데이트
    for cat in formulas_data.get('categories', []):
        for formula in cat.get('formulas', []):
            if formula.get('id') == formula_id:
                if image_path:
                    formula['image'] = image_path
                else:
                    formula.pop('image', None)
                
                # 변경사항 저장
                save_formulas(formulas_data)
                
                return jsonify({
                    'success': True,
                    'formula': formula
                })
    
    return jsonify({'error': '공식을 찾을 수 없습니다.'}), 404

# 모든 공식 목록 조회 (이미지 관리용)
@app.route('/api/formulas')
def api_formulas():
    data = load_formulas()
    formulas_list = []
    for cat in data.get('categories', []):
        for formula in cat.get('formulas', []):
            formulas_list.append({
                'id': formula.get('id'),
                'name': formula.get('name'),
                'category': cat.get('name'),
                'image': formula.get('image', '')
            })
    return jsonify(formulas_list)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug, host='0.0.0.0', port=port)

