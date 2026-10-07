def create_profile(name,*skills,**details):
    print("name:",name)
    print("skills:",skills)
    for skill in skills:
        print(skill)
    for key,value in details.items():
        print(key,":",value)
create_profile("nithu","python","java","c","html",age=21,city="Nizamabad",experience=2)
