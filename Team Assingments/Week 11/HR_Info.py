# with open('hr_system.txt') as hr_file:
    
#     for hr_data in hr_file:
#         hr_refined = hr_data.split(' ')
#         hr_names = hr_refined[0]
#         hr_id = hr_refined[1]
#         hr_job_title = hr_refined[2]
#         hr_salary = float(hr_refined[3])
#         hr_paycheck = (hr_salary / 15 )
        
#         if hr_job_title == 'Engineer':
#             hr_paycheck = (hr_salary / 15) + 1000
                
#         print (f'{hr_names} (ID: {hr_id}), {hr_job_title} - ${hr_paycheck:.2f}')
        
with open('hr_system.txt') as hr_file:
    
    for hr_info in hr_file:
        info_split = hr_info.split(' ')
        info_name = info_split[0]
        info_id = info_split[1]
        info_job = info_split[2]
        info_salary = float(info_split[3])
        person_paycheck = info_salary / 15.5
        
        if info_job == 'Engineer':
            person_paycheck  = (info_salary / 15.5) + 1000
            print(f'{person_paycheck}*')
        
        print (f'{info_name.strip()} (ID: {info_id.strip()}), {info_job.strip()} - ${person_paycheck:.2f}')