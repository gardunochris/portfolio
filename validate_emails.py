import re

EMAILS = [
    "abby@emergencydisasterservices.com",
    "cody@emergencydisasterservices.com",
    "jerry@emergencydisasterservices.com",
    "JBrandt@garner-es.com",
    "cbreckenridge@slsco.com",
    "Emendel@texasdisposal.com",
    "jordan@grannysalliance.com",
    "cwalker@garner-es.com",
    "Michaelh@employeehousing.com",
    "seth@employeehousing.com",
    "doug@grannysalliance.com",
    "b.alphin@industrialentsystems.com",
    "lucas@apexsites.com",
    "kbatey@teamhousing.com",
    "paul.switzer@atco.com",
    "eddie@kellymobilecity.com",
    "r.cheek@industrialentsystems.com",
    "ron@emergencydisasterservices.com",
    "don.brazil@usaupstar.com",
    "klay.south@usaupstar.com",
    "krodriguez@propacusa.com",
    "blakef@phoenixpollution.com",
    "jed.smith@rvbtransport.com",
    "erogers@texaspridedisposal.com",
    "npompa@propacusa.com",
    "mochoa@rruniversalsolutions.com",
    "jchavez@rruniversalsolutions.com",
]

pattern = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9._%+-]*[A-Za-z0-9])?@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

report = []
for email in EMAILS:
    if pattern.match(email):
        report.append(f"VALID: {email}")
    else:
        reason = []
        if '@' not in email:
            reason.append("missing '@'")
        if email.startswith('@') or email.endswith('@'):
            reason.append("missing local or domain part")
        if not re.search(r"\.[A-Za-z]{2,}$", email):
            reason.append("domain TLD missing or too short")
        if not reason:
            reason.append("does not match standard email format")
        report.append(f"INVALID: {email} - {'; '.join(reason)}")

if __name__ == "__main__":
    print("Email Validation Report:\n")
    for line in report:
        print(line)
