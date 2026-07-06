# SmartBuy User Flow

This document describes how users interact with SmartBuy from the moment they visit the website until they purchase a product using SmartBuy's recommendations.

## User Journey

### 1. New User Visits SmartBuy

Visitor

↓

Opens SmartBuy Website

↓

Views Landing Page

↓

Learns about SmartBuy

↓

Clicks **Get Started**

↓

Register / Login

### 2. Registration

User enters:

- Full Name
- Email Address
- Password

↓

Create Account

↓

Account Created Successfully

↓

Redirect to Dashboard

### 3. Login

User enters:

- Email
- Password

↓

Validate Credentials

↓

If valid

↓

Dashboard

Else

↓

Show "Invalid Email or Password"

↓

Try Again
### 4. Dashboard

The dashboard displays:

- Welcome Message
- Tracked Products
- Current Recommendations
- Recent Notifications
- Savings Summary
- Add Product Button
  

  ### 5. Track a Product

User clicks:

Add Product

↓

Paste Product URL

↓

Click Track Product

↓

SmartBuy validates the URL

↓

Extracts Product Information

↓

Saves Product

↓

Starts Background Price Monitoring

↓

Redirects to Product Details

### 6. URL Validation

User submits a product URL

↓

SmartBuy validates the URL

↓

Is the URL supported?

YES
↓

Extract Product Information

NO
↓

Display an error message

↓

Ask the user to enter a valid product URL

### 7. Product Information

After a valid product URL is submitted, SmartBuy extracts:

- Product Name
- Current Price
- Product Image
- Product Category
- Website Name
- Product Availability

↓

Display Product Preview

↓

User confirms tracking

↓

Product is added to the watchlist

### 8. Background Monitoring

Once the product is added:

↓

SmartBuy schedules automatic price checks

↓

Checks the product price every 2 hours

↓

Stores every price in the database

↓

Updates price history automatically

↓

Runs the recommendation engine

### 9. Recommendation Engine

SmartBuy analyzes:

- Current Price
- Historical Prices
- Price Trend
- Average Price
- Lowest Recorded Price
- Highest Recorded Price

↓

Generate Recommendation

Possible Results:

- Buy Now
- Wait
- Continue Monitoring

↓

Explain why the recommendation was made

### 10. Notification Flow

Should the user be notified?

↓

YES

↓

Send Email Notification

↓

User opens SmartBuy

↓

Views recommendation

↓

Decides whether to purchase

OR

↓

NO

↓

Continue monitoring the product

### 11. User Decision

User receives the notification

↓

Opens SmartBuy

↓

Views Product Details

↓

Reads SmartBuy Recommendation

↓

Chooses one of the following:

- Buy Product
- Continue Monitoring
- Remove Product from Watchlist

↓

Recommendation history is saved

## Possible Error Scenarios

### Invalid Product URL

- Display "Invalid product URL."
- Ask the user to enter a supported product link.

### Product Not Available

- Notify the user that the product is currently unavailable.
- Continue monitoring until the product becomes available again.

### Website Structure Changed

- Log the scraping error.
- Notify the administrator.
- Inform the user that price updates are temporarily unavailable.

### Network Failure

- Retry automatically.
- Continue monitoring later.

### Duplicate Product

- Detect if the user is already tracking the product.
- Ask whether they want to update notification settings instead of creating another entry.