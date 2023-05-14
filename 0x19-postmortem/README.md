My First Postmortem


Issue Summary: 

On May 12th, 2022, from 2:00 PM to 4:00 PM EST, our company's online payment system experienced an outage that impacted 30% of our users. The service was completely unavailable, and users could not complete any transactions during the outage.

Timeline:

2:00 PM: The outage was detected through monitoring alerts.
2:05 PM: The engineering team was alerted and began investigating the issue.
2:15 PM: The team identified that a database connection problem caused the issue.
2:30 PM: The team initially focused on debugging the application code responsible for the database connection but later discovered that the root cause was a misconfiguration in the database connection pool.
3:00 PM: The team realised that the initial debugging efforts were misdirected and shifted their focus to investigating the database configuration.
3:30 PM: The team identified the misconfiguration and resolved the issue by updating the database connection pool settings.
4:00 PM: The service was restored, and users could complete transactions again.

Root Cause and Resolution: 

The outage's root cause was a misconfiguration in the database connection pool. The connection pool was configured with too few connections, causing it to become overwhelmed during peak usage periods. This resulted in connections being refused, which caused the application to fail.
To resolve the issue, the team updated the connection pool settings to increase the number of available connections and prevent future outages.
Corrective and Preventative Measures: To prevent future outages, the team will implement the following corrective and preventative measures:

Conduct a thorough review of all database connection pool configurations to ensure they are optimised for peak usage periods.
Improve monitoring and alerting to detect similar issues in the future quickly.
Increase redundancy in the system to minimise the impact of future outages.
Schedule regular reviews and updates of all system configurations to ensure they are optimised and up-to-date.

In conclusion, the outage on May 12th, 2022, was caused by a misconfiguration in the database connection pool. The engineering team responded quickly and resolved the issue by updating the connection pool settings. To prevent similar outages in the future, the team will implement corrective and preventative measures to optimise system configurations, improve monitoring and alerting, and increase redundancy.
