POSTMORTEM: PROJECT ARTIMUS OUTAGE INCIDENT
Project Artimus faced an outage incident on June 1st, 2023 lasting almost two and half hours from 9:00 AM to 11:30 PM (GMT).
The web testing service of Project Artimus was unavailable during the outage period. Users experienced inability to submit test requests and access test results. Approximately 40% of the users were affected.
 
Timeline:
•	Issue Detection: The issue was detected at 9:00 AM (GMT) when monitoring systems triggered alerts for service unavailability.
•	Actions Taken: Immediately we started working on the incident. Initial investigation focused on network connectivity and server infrastructure. Assumptions were made that a network misconfiguration or server failure could be causing the issue.
•	Misleading Investigation: The investigation initially explored network and server logs, but no anomalies were found. Attention then shifted to database performance, leading to time-consuming troubleshooting efforts in that area.
•	Escalation: As the issue persisted, the incident was escalated as I blamed my colleague for the database administration and he also blaming me to be responsible for the web testing service.
•	Incident Resolution: At 11:30 PM (GMT), the root cause was identified and resolved, restoring the functionality of the web testing service. 
 
Root Cause and Resolution:
•	Root Cause: The outage was caused by a misconfigured firewall rule that blocked incoming traffic to the web testing service.
•	Resolution: The misconfigured firewall rule was identified and corrected. Our DevOps knowledge came into being as we updated the firewall configuration to allow the necessary traffic. This restored service availability.
 
Corrective and Preventative Measures:
•	Improvements/Fixes: 
1.	Strengthen firewall rule management processes to prevent misconfigurations.
2.	Enhance monitoring capabilities to detect and alert on firewall rule changes.
3.	Implement automated deployment and configuration management tools to reduce manual errors.

•	Tasks to Address the Issue:
1.	Review and update firewall rule management procedures to ensure thorough testing and validation.
2.	Enhance monitoring systems to provide real-time alerts for firewall rule changes.
3.	Conduct a comprehensive audit of all firewall rules to identify and rectify potential misconfigurations.
4.	Implement infrastructure automation tools to streamline deployment and minimize human error.
 
In conclusion, the outage of the web testing service in Project Artimus was caused by a misconfigured firewall rule. Through investigation and escalation, the root cause was identified and resolved, restoring service availability. To prevent similar incidents in the future, measures will be taken to strengthen firewall rule management and enhance monitoring capabilities. Implementing automation and conducting thorough audits will further mitigate the risk of misconfigurations.
