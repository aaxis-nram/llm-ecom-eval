=E2&IF(F2<>"",","&F2&IF(G2<>"",", "&G2&IF(H2<>"",", "&H2,""),""),"")

In the data section is a list of tickets for customer support.
Rewrite the ticket description removing any text that appears to be from a template and is repeating in each ticket. Make the customer request sound natural.
Output the most likely ticket type and ticket subtype for each request from the ticket_types provided.
Examine the ticket description and identify which of the products in the list best fit the problem, then output the product.
Pick lines that have good enough detail to identify ticket type, subtype, and product
Replace the product_purchased in the ticket description with the product selected.

Output format CSV with columns Ticket ID, Ticket Type, Ticket Subtype, Product, Ticket Description
Enclose all columns in double-quotes.

---
In the data section is a list of tickets for customer support.
Only output the tickets that appear to be legitimate customer requests.
Rewrite the ticket description removing any text that appears to be from a template and is repeating in each ticket. Make the customer request sound natural.
Output the most likely ticket type and ticket subtype for each request from the ticket_types provided.
Output the most likely products from the products provided.

Output format JSON with keys Ticket ID, Ticket Type, Ticket Subtype, Product, Ticket Description

<ticket_types>
{
  "Billing Inquiry": [
    "Account Access",
    "Payment Issue",
    "Refund Request",
    "Cancellation Request",
    "Product Inquiry"
  ],
  "Product Inquiry": [
    "Product Recommendation",
    "Product Compatibility",
    "Peripheral Compatibility",
    "Product Setup"
  ],
  "Technical Issue": [
    "Account Access",
    "Software Bug",
    "Hardware Issue",
    "Network Problem",
    "Installation Support",
    "Data Loss",
    "Display Issue",
    "Battery Life",
    "Delivery Problem"
  ],
  "Unknown": [
    "Unknown"
  ]
}
</ticket_types> 
<products>
[
  "GoPro Hero",
  "LG Smart TV",
  "Dell XPS",
  "Microsoft Office",
  "Autodesk AutoCAD",
  "Microsoft Surface",
  "Philips Hue Lights",
  "Fitbit Versa Smartwatch",
  "Dyson Vacuum Cleaner",
  "Nintendo Switch",
  "Microsoft Xbox Controller",
  "Nintendo Switch Pro Controller",
  "Nest Thermostat",
  "Sony PlayStation",
  "GoPro Action Camera", 
  "Xbox",
  "LG Washing Machine",
  "Canon EOS",
  "HP Pavilion",
  "Amazon Kindle",
  "Lenovo ThinkPad",
  "Fitbit Charge",
  "Adobe Photoshop",
  "Google Pixel",
  "Amazon Echo",
  "PlayStation",
  "Samsung Galaxy",
  "iPhone",
  "LG OLED",
  "Sony Xperia",
  "Apple AirPods",
  "Sony 4K HDR TV",
  "Canon DSLR Camera",
  "Roomba Robot Vacuum",
  "Nikon D",
  "Bose QuietComfort",
  "Samsung Soundbar",
  "Asus ROG",
  "Bose SoundLink Speaker",
  "Google Nest", 
  "Garmin Forerunner",
  "MacBook Pro"
]
</products>

<data>
[
{"Ticket ID": "1", "Ticket Description": "I'm having an issue with the {product_purchased}. Please assist.\n\nYour billing zip code is: 71701.\n\nWe appreciate that you have requested a website address.\n\nPlease double check your email address. I've tried troubleshooting steps mentioned in the user manual, but the issue persists."},
{"Ticket ID": "2", "Ticket Description": "I'm having an issue with the {product_purchased}. Please assist.\n\nIf you need to change an existing product.\n\nI'm having an issue with the {product_purchased}. Please assist.\n\nIf The issue I'm facing is intermittent. Sometimes it works fine, but other times it acts up unexpectedly."},
{"Ticket ID": "3", "Ticket Description": "I'm facing a problem with my {product_purchased}. The {product_purchased} is not turning on. It was working fine until yesterday, but now it doesn't respond.\n\n1.8.3 I really I'm using the original charger that came with my {product_purchased}, but it's not charging properly."},
{"Ticket ID": "4", "Ticket Description": "I'm having an issue with the {product_purchased}. Please assist.\n\nIf you have a problem you're interested in and I'd love to see this happen, please check out the Feedback. I've already contacted customer support multiple times, but the issue remains unresolved."},
{"Ticket ID": "5", "Ticket Description": "I'm having an issue with the {product_purchased}. Please assist.\n\n\nNote: The seller is not responsible for any damages arising out of the delivery of the battleground game. Please have the game in good condition and shipped to you I've noticed a sudden decrease in battery life on my {product_purchased}. It used to last much longer."},
{"Ticket ID": "6", "Ticket Description": "I'm facing a problem with my {product_purchased}. The {product_purchased} is not turning on. It was working fine until yesterday, but now it doesn't respond. To remove the new {product_purch I've checked for any available software updates for my {product_purchased}, but there are none."},
{"Ticket ID": "7", "Ticket Description": "I'm unable to access my {product_purchased} account. It keeps displaying an 'Invalid Credentials' error, even though I'm using the correct login information. How can I regain access to my account?\n\nSolution 1 I'm unable to find the option to perform the desired action in the {product_purchased}. Could you please guide me through the steps?"},
{"Ticket ID": "8", "Ticket Description": "I'm having an issue with the {product_purchased}. Please assist. (Thanks) I will contact all my suppliers and confirm.\n\nPlease try and find out whether their inventory is currently stocked, or any other reason. I am I've performed a factory reset on my {product_purchased}, hoping it would resolve the problem, but it didn't help."},
{"Ticket ID": "9", "Ticket Description": "I'm having an issue with the {product_purchased}. Please assist. Thank you.\n\n{product_purchased} is not the exact type you might prefer, they use the exact same method for different uses. Please help I've recently updated the firmware of my {product_purchased}, and the issue started happening afterward. Could it be related to the update?"},
{"Ticket ID": "10", "Ticket Description": "My {product_purchased} is making strange noises and not functioning properly. I suspect there might be a hardware issue. Can you please help me with this?\n\n} If we can, please send a \"request\" to dav The issue I'm facing is intermittent. Sometimes it works fine, but other times it acts up unexpectedly."},
{"Ticket ID": "11", "Ticket Description": "I'm having an issue with the {product_purchased}. Please assist. 1-800-799-0808.\n\nProduct Search: What's New in 2-3-4-5? Report Feedback Customer Service is your best I'm using the original charger that came with my {product_purchased}, but it's not charging properly."},
]
</data>

---
In each of the lines below, determine if ticket type represents a realistic customer message. Output one line per ticket in JSON format with Ticket ID, Looks Real (Yes/No), Ticket Type, Ticket Subject and Ticket Description.
<data>
{'Ticket ID': '1', 'Ticket Type': 'Technical issue', 'Ticket Subject': 'Product setup', 'Ticket Description': "I'm having an issue with the {product_purchased}. Please assist.\n\nYour billing zip code is: 71701.\n\nWe appreciate that you have requested a website address.\n\nPlease double check your email address. I've tried troubleshooting steps mentioned in the user manual, but the issue persists."}
{'Ticket ID': '2', 'Ticket Type': 'Technical issue', 'Ticket Subject': 'Peripheral compatibility', 'Ticket Description': "I'm having an issue with the {product_purchased}. Please assist.\n\nIf you need to change an existing product.\n\nI'm having an issue with the {product_purchased}. Please assist.\n\nIf The issue I'm facing is intermittent. Sometimes it works fine, but other times it acts up unexpectedly."}
</data>

---

Here is a list of Ticket Types and Ticket Subtype. Output a list of ticket types and ticket sub types. Only output ticket sub types that makes sense with the ticket type. A ticket subtype make appear under multiple Ticket types if appropriate
Output format:
Ticket Type, Ticket Subtype
Billing Inquiry, Account Access
<data>
Ticket Type	Ticket Subtype
Billing inquiry	Account access
Billing inquiry	Battery life
Billing inquiry	Cancellation request
Billing inquiry	Data loss
Billing inquiry	Delivery problem
Billing inquiry	Display issue
Billing inquiry	Hardware issue
Billing inquiry	Installation support
Billing inquiry	Network problem
Billing inquiry	Payment issue
Billing inquiry	Peripheral compatibility
Billing inquiry	Product compatibility
Billing inquiry	Product recommendation
Billing inquiry	Product setup
Billing inquiry	Refund request
Billing inquiry	Software bug
Refund request	Account access
Refund request	Battery life
Refund request	Cancellation request
Refund request	Data loss
Refund request	Delivery problem
Refund request	Display issue
Refund request	Hardware issue
Refund request	Installation support
Refund request	Network problem
Refund request	Payment issue
Refund request	Peripheral compatibility
Refund request	Product compatibility
Refund request	Product recommendation
Refund request	Product setup
Refund request	Refund request
Refund request	Software bug
Cancellation request	Account access
Cancellation request	Battery life
Cancellation request	Cancellation request
Cancellation request	Data loss
Cancellation request	Delivery problem
Cancellation request	Display issue
Cancellation request	Hardware issue
Cancellation request	Installation support
Cancellation request	Network problem
Cancellation request	Payment issue
Cancellation request	Peripheral compatibility
Cancellation request	Product compatibility
Cancellation request	Product recommendation
Cancellation request	Product setup
Cancellation request	Refund request
Cancellation request	Software bug
Product inquiry	Account access
Product inquiry	Battery life
Product inquiry	Cancellation request
Product inquiry	Data loss
Product inquiry	Delivery problem
Product inquiry	Display issue
Product inquiry	Hardware issue
Product inquiry	Installation support
Product inquiry	Network problem
Product inquiry	Payment issue
Product inquiry	Peripheral compatibility
Product inquiry	Product compatibility
Product inquiry	Product recommendation
Product inquiry	Product setup
Product inquiry	Refund request
Product inquiry	Software bug
Technical issue	Account access
Technical issue	Battery life
Technical issue	Cancellation request
Technical issue	Data loss
Technical issue	Delivery problem
Technical issue	Display issue
Technical issue	Hardware issue
Technical issue	Installation support
Technical issue	Network problem
Technical issue	Payment issue
Technical issue	Peripheral compatibility
Technical issue	Product compatibility
Technical issue	Product recommendation
Technical issue	Product setup
Technical issue	Refund request
Technical issue	Software bug
</data>

