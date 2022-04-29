from demands import *

@app.route('/demands', methods=['GET'])
@cross_origin()
def get_demands():
    return jsonify({'demands': Demand.get_all_demands()})

@app.route('/demands/<int:id>', methods=['GET'])
@cross_origin()
def get_demand(id):
    return jsonify({'demand': Demand.get_demand(id)})

@app.route('/demands', methods=['POST'])
@cross_origin()
def add_demand():    
    data = request.json
    Demand.add_demand(data['company_name'], data['applicant_names'], data['phone_number'], data['company_email'], data['solution_type'], data['reffered_by'], data['additional_comments'])
    response = Response("Demand added", status=201, mimetype='application/json')
    return response

@app.route('/demands/<int:id>', methods=['PUT'])
@cross_origin()
def update_demand(id):
    data = request.json
    Demand.update_demand(id, data['company_name'], data['applicant_names'], data['phone_number'], data['company_email'], data['solution_type'], data['reffered_by'], data['additional_comments'])
    response = Response("Demand updated", status=201, mimetype='application/json')
    return response

@app.route('/demands/<int:id>', methods=['DELETE'])
@cross_origin()
def delete_demand(id):
    Demand.delete_demand(id)
    response = Response("Demand deleted", status=201, mimetype='application/json')
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5000)
