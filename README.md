# SmartBuy

**Know When to Buy.**

## Overview

SmartBuy is a web application that helps users make better purchasing decisions instead of simply tracking product prices.

Most price trackers only notify users when a product reaches a specific price. SmartBuy goes a step further by continuously monitoring product prices, maintaining historical price records, analyzing trends, and recommending whether it is a good time to buy or if waiting may result in a better deal.

The objective is not to predict the exact future price of a product, but to help users make informed buying decisions using available data.

## Problem Statement

Many people spend days or even weeks checking online shopping websites before purchasing expensive products such as laptops, phones, headphones, or gaming devices.

Although price tracking tools exist, they usually provide only price alerts and leave the buying decision entirely to the user.

SmartBuy aims to solve this problem by collecting historical price information, monitoring price changes automatically, and providing intelligent recommendations about the best time to purchase a product.

## Objectives

The main objectives of SmartBuy are:

- Monitor product prices automatically.
- Build a historical price database.
- Analyze price trends over time.
- Recommend whether users should buy now or wait.
- Notify users when a product reaches a favorable buying opportunity.
- Present all information through a simple and interactive web interface.

## Core Features

### User Management

- User registration and login
- Secure authentication
- Personal dashboard

### Product Tracking

- Add products using product URLs
- Automatically extract product information
- Save products to a personal watchlist

### Price Monitoring

- Monitor prices automatically
- Store historical price data
- Show current, lowest, highest, and average prices
- Detect price drops

### Recommendation Engine

SmartBuy analyzes:

- Current price
- Historical prices
- Price trend
- Price volatility
- Average price
- Previous discounts

Based on this analysis, SmartBuy recommends one of the following:

- Buy Now
- Wait
- Continue Monitoring

Each recommendation includes an explanation so users understand why it was made.

### Notifications

Users receive notifications when:

- A target price is reached
- SmartBuy recommends purchasing
- A significant price drop is detected

Notifications will initially be sent through email, with Telegram and browser notifications planned for future versions.

### Dashboard

The dashboard allows users to:

- View tracked products
- Monitor price history
- View recommendations
- See recent notifications
- Track estimated savings


## Technology Stack

### Frontend

- React
- Vite
- Tailwind CSS

### Backend

- Python
- FastAPI

### Database

- PostgreSQL

### Web Scraping

- BeautifulSoup
- Playwright

### Background Jobs

- APScheduler

### Machine Learning

- Scikit-learn

### Authentication

- JWT

### Deployment

- Docker
- Render


## Development Roadmap

### Version 1

- User authentication
- Product tracking
- Dashboard
- Automatic price monitoring
- Email notifications

### Version 2

- Historical price analytics
- Interactive charts
- Recommendation engine
- Deal score

### Version 3

- Machine learning based recommendations
- Multi-store comparison
- Telegram notifications

### Version 4

- Mobile application
- Browser extension
- Personalized shopping insights

## Project Goals

This project is being developed to strengthen practical knowledge in:

- Software Engineering
- Backend Development
- Frontend Development
- Database Design
- REST API Development
- Web Scraping
- Background Scheduling
- Machine Learning
- Cloud Deployment
- Docker
- Git and GitHub

## Future Improvements

Some planned improvements include:

- Browser extension
- Mobile application
- Multi-store price comparison
- AI shopping assistant
- Personalized recommendations
- Budget planning
- Push notifications


## Current Status

SmartBuy is currently under active development.

The project is being built as a complete end-to-end web application while following modern software engineering practices.


## Author

Sai Praneeth

B.Tech Student

This project is being developed as part of my journey to become a software engineer by building a real-world product from scratch.

## License

This project is licensed under the MIT License.