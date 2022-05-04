from demands import *

for i in range(1, 100):
    Demand.add_demand('company_name' + str(i), 'applicant_names' + str(i), '(123)123-4125', 'email@company_email.com' + str(i), 'solution_type' + str(i), 'Freight_Factoring', 'additional_comments' + str(i))
    
