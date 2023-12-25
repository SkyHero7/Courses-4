class Vacancy:
    def __init__(self, id, name, department, has_test, response_letter_required, area, type, address, response_url,
                 sort_point_distance, published_at, created_at, archived, apply_alternate_url, insider_interview,
                 url, alternate_url, relations, employer, snippet, premium, salary, contacts, schedule, working_days,
                 working_time_intervals, working_time_modes, accept_temporary, professional_roles,
                 accept_incomplete_resumes, experience, employment, adv_response_url, is_adv_vacancy, adv_context,
                 show_logo_in_search=None, branding=None):
        self.id = id
        self.name = name
        self.department = department
        self.has_test = has_test
        self.response_letter_required = response_letter_required
        self.area = area
        self.type = type
        self.address = address
        self.response_url = response_url
        self.sort_point_distance = sort_point_distance
        self.published_at = published_at
        self.created_at = created_at
        self.archived = archived
        self.apply_alternate_url = apply_alternate_url
        self.insider_interview = insider_interview
        self.url = url
        self.alternate_url = alternate_url
        self.relations = relations
        self.employer = employer
        self.snippet = snippet
        self.premium = premium
        self.salary = salary
        self.contacts = contacts
        self.schedule = schedule
        self.working_days = working_days
        self.working_time_intervals = working_time_intervals
        self.working_time_modes = working_time_modes
        self.accept_temporary = accept_temporary
        self.professional_roles = professional_roles
        self.accept_incomplete_resumes = accept_incomplete_resumes
        self.experience = experience
        self.employment = employment
        self.adv_response_url = adv_response_url
        self.is_adv_vacancy = is_adv_vacancy
        self.adv_context = adv_context
        self.show_logo_in_search = show_logo_in_search
        self.branding = branding















    def __str__(self):
        return f"{self.title}, {self.salary}"