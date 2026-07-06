# SmartBuy Pages

This document describes every page in the SmartBuy application, its purpose, and the components displayed on each page.

## 1. Landing Page

---

# 2. Dashboard

## Purpose

The Dashboard is the central workspace of SmartBuy. It allows users to quickly track new products, monitor existing products, view recommendations, and receive important price alerts.

The dashboard should immediately guide users toward their next action without overwhelming them with unnecessary information.

---

## Layout

The dashboard consists of:

- Navigation Sidebar
- Welcome Section
- Product URL Input
- Tracked Products
- Recent Recommendations
- Notifications
- Quick Statistics

---

## Welcome Section

Display a personalized greeting.

Example:

Welcome back, Praneeth 👋

Your personal shopping companion.

Track products, monitor prices, and know exactly when it's the right time to buy.

---

## Product URL Input

This should be the first interactive component users see.

Input Placeholder:

Paste an Amazon or Flipkart product link...

Button:

Analyze Product

After clicking Analyze Product:

- Validate URL
- Extract product information
- Show product preview
- Ask for confirmation
- Start monitoring

---

## Tracked Products

Display products as clean cards.

Each card should contain:

- Product Image
- Product Name
- Current Price
- Recommendation
- Last Updated
- View Details Button

---

## Recent Recommendations

Display the latest AI recommendations.

Example:

MacBook Air

BUY NOW

Lowest price in the last 45 days.

--------------------------------

Sony WH-1000XM6

WAIT

Price has been falling steadily.

--------------------------------

RTX 5070

CONTINUE MONITORING

Not enough historical data.

---

## Notifications

Display recent notifications.

Example:

Today

MacBook Air reached your target price.

--------------------------------

Yesterday

Sony Headphones dropped 12%.

--------------------------------

2 Days Ago

Price monitoring started for RTX 5070.

---

## Quick Statistics

Show small summary cards.

Examples:

Products Tracking

Average Savings

Buy Now Recommendations

Products Being Monitored

---

## Design Principles

The dashboard should:

- Feel clean and minimal.
- Guide the user naturally.
- Never appear crowded.
- Prioritize important information.
- Encourage users to track more products.

---

# 3. Product Analysis Page

## Purpose

The Product Analysis page is the heart of SmartBuy.

It provides detailed information about a tracked product, including price history, recommendations, analytics, reviews, and historical trends. This page helps users confidently decide whether to buy the product now or continue monitoring it.

---

## Layout

The page is divided into two sections.

Left Side

- Product Image
- Product Gallery
- Product Name
- Brand
- Product Description
- Rating
- Number of Reviews
- Product Specifications
- Buy on Website Button

Right Side

- Current Price
- Historical Price Graph
- Lowest Recorded Price
- Highest Recorded Price
- Average Price
- Deal Score
- SmartBuy Recommendation
- Recommendation Reason
- Confidence Score
- Overall Reviews

---

## Product Information

Display

- Product Name
- Product Images
- Current Price
- Original Price
- Discount Percentage
- Rating
- Number of Ratings
- Product Description
- Available Variants

---

## Price Analytics

Display

- Current Price
- Lowest Price
- Highest Price
- Average Price
- Price Difference
- Last Updated

Display an interactive graph for

- 7 Days
- 30 Days
- 90 Days
- 1 Year

---

## SmartBuy Recommendation

Recommendation Card

Recommendation

BUY NOW / WAIT / CONTINUE MONITORING

Confidence

Example

92%

Reason

Explain why SmartBuy made this recommendation.

Example

The current price is the lowest recorded in the last 45 days.

The price is currently 13% below the historical average.

Based on previous pricing patterns, waiting is unlikely to provide significant additional savings.

---

## Deal Score

Display a score from 0–100.

Example

92 / 100

Categories

90–100 Excellent Deal

70–89 Good Deal

50–69 Fair Price

Below 50 Expensive

---

## Community Reviews

Display

Overall Rating

Number of Reviews

Most Mentioned Positives

Most Mentioned Negatives

Review Distribution

Example

★★★★★ 4.6

18,742 Reviews

Most Liked

- Battery Life
- Display
- Performance

Needs Improvement

- Heating
- Camera

---

## Monitoring Information

Display

Monitoring Started

Last Checked

Next Scheduled Check

Notification Status

Tracking Duration

---

## Available Actions

Buttons

- Buy Now
- Continue Monitoring
- Remove from Watchlist
- Share Product

---

# 4. Notifications

## Purpose

The Notifications page keeps users informed about important updates regarding the products they are tracking.

Notifications should only appear when they provide meaningful information to the user.

---

## Layout

Each notification card contains:

- Product Image
- Product Name
- Notification Type
- Short Description
- Date & Time
- Action Button

---

## Notification Types

### Buy Now

SmartBuy recommends purchasing this product.

Example:

MacBook Air M4

BUY NOW

Current price is the lowest recorded in the last 45 days.

Confidence: 92%

[ View Product ]

---

### Price Drop

Sony WH-1000XM6

Price dropped by 12%

Current Price

₹21,999

[ View Details ]

---

### Target Price Reached

The product has reached your target price.

Current Price

₹49,999

Target Price

₹50,000

---

### Monitoring Started

SmartBuy has started monitoring your product.

We'll notify you whenever something important happens.

---

### Product Unavailable

This product is currently unavailable.

Monitoring will continue automatically.

---

# 5. Profile

## Purpose

Allow users to manage their SmartBuy account.

---

Display

- Name
- Email
- Joined Date
- Products Tracked
- Estimated Savings
- Recommendations Followed

---

## Settings

- Change Password
- Notification Preferences
- Dark Mode
- Delete Account

---

# 6. Settings

## Notification Preferences

Email Notifications

On / Off

Target Price Notifications

On / Off

SmartBuy Recommendations

On / Off

Price Drop Alerts

On / Off

Weekly Summary

On / Off

---

## Monitoring

Monitoring Frequency

Balanced (Default)

Aggressive

Battery Saver

---

## Appearance

Light Mode

Dark Mode

System Theme

---

## Privacy

Export Data

Delete Account