MY FIRST POSTMORTEM

Server failure report

On February 22, 2023, from 9:00 PM to 11:30 PM EST, our hospital management system website experienced an outage that affected 37% of our users. During the outage, users were unable to access the website, browse appointments, patients were not able to access their medical information and the inventory manager couldn’t manage shortages since the website was off to report the shortage. The root cause of the issue was a database failure that caused the website to become unresponsive.

Timeline

9:00 PM: The issue was detected when our monitoring system alerted us of increased error rates and server latency.
9:05 PM: Our engineering team began investigating the issue, assuming it was a server overload due to increased traffic.
9:20 PM: After ruling out server overload, the team suspected a database issue and began investigating the database servers.
9:40 PM: The team identified a hardware failure on one of the database servers and attempted to failover to a backup server.
10:00 PM: The failover attempt was unsuccessful, and the team escalated the incident to the database administration team.
10:30 PM: The database administration team diagnosed the issue as a corrupt database file and began restoring from a backup.
11:00 PM: The database was successfully restored, and the website began to recover.
11:30 PM: The website was fully restored, and all users were able to access the website and complete tasks.

Root Cause and Resolution

The root cause of the issue was a corrupt database file that caused the primary database server to become unresponsive. The database administration team identified and resolved the issue by restoring from a backup.

Corrective and Preventative Measures

To prevent similar issues in the future, we will be implementing the following measures:

Improve database monitoring to detect and alert us of potential issues before they become critical.
Implement a more robust backup and disaster recovery plan to ensure minimal downtime in the event of a database failure.
Perform regular database maintenance to prevent corruption and optimize performance.
Improve communication and escalation processes to ensure a more efficient incident response.



# MAKOHA DHARREN PIUS (AUTHOR) # 





