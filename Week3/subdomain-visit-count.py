class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_visits = collections.defaultdict(int)
        for cpdomain in cpdomains:
            cpdomain = cpdomain.split()
            visit_count = int(cpdomain[0])
            domains = cpdomain[1].split('.')[::-1]
            
            domain_name = ''
            for domain in domains:
                if domain_name == '':
                    domain_name = domain
                else:
                    domain_name = domain + '.' + domain_name
                domain_visits[domain_name] += visit_count
            
            results = list()
            for result in domain_visits:
                results.append(str(domain_visits[result]) + ' ' + result)
        return results