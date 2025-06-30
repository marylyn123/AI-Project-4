TASK 2 SUMMARY
Using AI-enhanced test automation tools significantly improves test coverage and maintenance. 
In this task, I automated login functionality using Testim.io testing both valid and invalid credential scenarios. 
The AI feature automatically detected UI element changes—like a renamed button ID—and updated the script without manual intervention. 
This reduced test flakiness and the need to frequently revise selectors. 
The tool also suggested edge cases, such as empty field submissions, which I hadn’t initially considered. 
After executing the test, I received a visual report with pass/fail results, time logs, and screenshots.
Compared to traditional manual testing, this approach increased accuracy, minimized human error, and accelerated execution time. 
Overall, AI testing tools help teams scale QA efforts while maintaining reliability across changing user interfaces.
### Part 3: Ethical Reflection

When deploying the predictive model for resource allocation, a key ethical concern is the potential for bias in the dataset. If certain teams or types of issues are underrepresented in the training data, the model may learn patterns that unfairly associate low priority with those teams. This can result in unequal treatment, where some teams consistently receive fewer resources or delayed responses—not because of the actual urgency of their issues, but due to biased historical data.

Such bias can be unintentional but harmful, especially if the model is retrained over time using the same skewed feedback loop. This may reinforce existing disparities, making it harder for affected teams to receive fair treatment.

To address this, tools like IBM AI Fairness 360 can be used. This toolkit helps:
- Detect bias by analyzing model outcomes across different groups.
- Measure fairness using metrics like disparate impact or statistical parity.
- Mitigate unfairness through techniques like reweighing the data or post-processing model predictions to reduce disparity.

By applying these fairness techniques, we can make the model more equitable, ensuring that predictions are based on actual issue characteristics rather than historical or structural biases. This promotes ethical AI use in software engineering, where decisions impact real people and teams.

