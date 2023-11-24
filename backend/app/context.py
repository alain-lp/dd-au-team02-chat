SWAP_CONTEXT_COMMAND = "set mode"

LIST_CONTEXT_COMMAND = "list modes"

LITTLEPAY_CONTEXT = """
## Business

Littlepay is a payment service provider that provides contactless and E-commerce payments for the mobility industry. 

Littlepay is a modular system that facilitates seamless integration with various device terminals, payment gateways and acquiring banks.

## Strengths and Benefits of Littlepay

******************************Speed to Market******************************

Switch on a contactless pilot within weeks using our cloud-based payment platform and your choice of our pre-integrated technology and banking partners.

************Attractive Pricing************

Littlepay makes contactless acceptance accessible to all transit operators and agencies. Rollout with a minimal upfront cost and competitive per-transaction fees.

**************************************************Multiple Validator Options**************************************************

Choose from our extensive range of pre-certified, ‘Littlepay Ready’ payment readers. If you don’t find the hardware you want, ask us about a new integration.

******Choice of Back-Office******

Let Littlepay handle tap aggregation, fare capping and fare calculation; or use our APIs to integrate an external back office to our payments platform.

**************Revenue Protection**************

With deny list management, automatic debt recovery and a revenue inspection app, Littlepay minimises losses through declines, fraud and fare evasion.

********************************************************Unified passenger experience********************************************************

Tokenisation of bank cards and mobile wallets used across our Contactless and Checkout payment channels enables a seamless travel experience.

************************************************Passenger-pleasing fares************************************************

Our configurable merchant portal allows you to set up a range of dynamic fare caps and discounts to bring tap-to-ride passengers automatic best value.

**************Built-in Compliance**************

Littlepay Contactless adheres to high standards of security and data privacy. It is PCI Level 1 compliant, and registered and approved by Visa as a partner for transit.

More than **250** transport operators use Littlepay.

Littlepay has **18** pre-integrated ticketing technology partners and **10** payment gateway and acquiring partners.
Littlepay is processing transactions in 12 countries and continuing to expand globally.

## Capability

Littlepay has approximately 90 staff spread across Australia and the UK divided into the following areas:

Operations: provides help and support to merchants and integration partners.

Commercial: 

Security: 

Engineering: There are approximately 45 engineers, responsible for building and maintaining the products and platforms that Littlepay offers. The engineers are divided up into the following teams:

- DevOps - maintains and secures infrastructure and supports the development efforts of the other teams
- Payments - Responsible for integrating against Acquirers to build systems that can authorise and take payments.
- Card Present - Builds and maintains the systems that are used by EMV devices to record taps and initiate transactions to collect fares based on those taps
- Ecommerce - builds and maintains the Checkout SDK and the APIs that allows merchants to create and manage online orders and payments
- Merchant experience - maintains littlepay control, the merchant portal

## Objectives

## Partners

## Services

## APIs

The following APIs and what they are used for are provided by Littlepay for customers to use:

The Checkout API: The Littlepay Checkout APIs provide a simple and secure way to accept online payments from front of office web and native mobile applications. It allows customers to create an ecommerce order to make a purchase, save cards for future purchases, manage their existing stored cards, allows merchants to refund a payment that has already been made and allows merchants to trigger regular payments for subscriptions or recurring payments. Merchants can use the Checkout API to initiate orders and payments and progress them through to completion. 

Back Office API: The Back Office API enables automated fare collection (AFC) systems to plug seamlessly into a Littlepay transaction flow without compromising security. Littlepay publish traveler's non-sensitive transaction data as they travel, allowing an integrated AFC to calculate fares and control payment. The Back Office API gives you the flexibility to calculate fares, issue charge instructions and manage risk. The Back Office API allows merchants to block cards by managing a deny list, recover debts that are outstanding, refund charges made for trips or orders, manage products and fare rules, view trips and orders made by the merchant's customers.

The Device API supports integration with EMV devices to detect when transit system passengers tap on or off at the start or end of their trips. It handles various mobility and transport transaction models, collecting fares and helps manage risk. The Device API can be sent tap events from EMV devices that represent transactions for retail purchases and known and variable fares. Devices can retrieve up to date deny lists that allow it to know what cards should be blocked or denied.

In addition to those APIs Littlepay provide a data feed for each merchant. These feeds enable access to raw data that is generated into an AWS S3 bucket in pipe-separated values (PSV file format). The data available through the feeds include payment authorisations, customer funding sources, device transactions, payments, adjustments, refunds, settlements and product data.

Littlepay also allow merchant integrators to subscribe to webhooks and receive events related to:

- Orders
- Transactions
- Payment sources
- Refunds
- Debts
- Changes in card status for cards used for taps

**********Merchant Experience**********

## Products

Littlepay offers these products to merchant customers:

**Littlepay Control**

Our merchant portal to track payments, create fare caps and discounts, carry out refunds and collect transaction data.

**Littlepay Analytics**

Supports analysis performance trends (sales, refunds, declines, debts) and customer behaviour – by zone, route, product or segment.

**Littlepay Products**

Give passengers a self-service customer portal (white label or API) to track journeys and transactions, and manage refunds.

**Littlepay Records**

Receive daily transaction data sets to feed into business intelligence, and use discoveries to underpin ticketing and payments strategy.

**Littlepay Inspect**

Install our fare inspection app on any NFC compatible, Android mobile device, to check passengers’ cards are verified for travel.

**Littlepay Checkout**

The core of Littlepay’s product offerings and a source of technical excellence, enables developers to build seamless, secure mobile checkouts for your transit website or app using our e-commerce APIs and SDKs. 

## Data

### Schemes of selected Conformed Tables

- MpsTaps - This contains the traveler’s bus tap ON or OFF information. This table has the description of each tap.
- Micropayments - This contains the trip information. This could be combined together with other micropayments which go together before being sent off to the bank (or acquirer) to process the payment.
- Aggregations - This is a group of micropayment which together are sent to the banks.
- Authorisations - This is the initial interaction with the bank wherein we ask if the card can process payment or we hold a certain amount on the .
- Settlement - This is the record the transfer of money from the banks to the bus operator and if they’re successful or not
- Product - Contains the rules for applying cap on the fares for travellers who travel frequently
- Micropayment Adjustment -
- Participant
"""

SERVICE_OPS_HELP_CONTEXT = """
Questions will be about how toset up fare configurations and capping in the merchant portals and the following information can be used to answer:

## Step 1. Configure a zone based on zone map

In this workshop, we will recreate a Brighton & Hove product, which is currently live in production.

### Network Map

There are two zones within this network

1. CitySAVER
2. networkSAVER

### **Daily Cap**

### citySAVER - citySAVER

On Peak: $6.5 Cap

Off Peak: $5.5 Cap

### networkSAVER - networkSAVER

On Peak: $6.5 Cap

Off Peak: $5.5 Cap

### citySAVER - networkSAVER

On Peak: $7.5

Off Peak: $6.5

### Configuring Zones

### 1. Go to the ‘Zones’ page

### 2. Select ‘Add new zone’

- Enter Zone Name: ‘citySAVER’
    - Enter ‘Capping Zone ID’: 1
    - Select ‘save’
- Enter Zone Name: ‘networkSAVER’
    - Enter ‘Capping Zone ID’: 2
    - Select ‘Save'

## Step 2. Set peak / off-peak price

### 1. Go to the ‘Pricing Period’ page

### **Field Breakdown**

Rule Name

- Set Rule Name to ‘Test’

Pricing Period Days

- Double click on the slider to create a new peak period
    - Morning Peak: Drag to 7:00 - 9:30
    - Afternoon Peak: Drag to 16:00 to 18:00

Save

- Select the Green save button

## Step 3. Creating a capping product

### 1. Got to the ‘capping’ page

- Select ‘Create Product’

---

### 2. Set Product Rules

### Product Status, Activation Type & Capping Type

**Product Status**

- [x]  `Enabled`
- [ ]  `Disabled`
- This field determines if the product is ‘active’ or 'inactive'

**Activation Type**

- [x]  `All Customers`

This field determines if all customers receive this capping product

- [ ]  `Registered Customers`

For scenarios where concession would be implemented by merchants and certain customers would be registered under concession.

**Capping Type**

- [x]  `Daily Capping`
- [ ]  `Weekly Capping`
- [ ]  `Multi-Day Capping`
- [ ]  `Time-Based Capping`
- This field determines the capping type / period this product is valid for see below for detail on each type.

---

### Product Code, Product Description, Cap Trigger Amount, Max Fare Amount

**Product Code**

Enter: `'yourname' test`

**Product Description**

Enter: `'yourname' Test`

**Cap Trigger Amount**

Enter: `5.5`

- This is the maximum a traveller will pay over the capping period of the product

**Max Fare Amount**

Enter: `5.5`

- This is the maximum fare amount that is eligible for the product

---

### All Day, Capping Period Overlap Time, Capping Start Time, Capping End Time & Timezone

**All Day**

Select: `YES`

- This sets the start and end time to a 24hr period. The overlap time allows the capping product to continue up to 5:00AM the following day

**Capping Start Time**

Keep as default

**Capping Endtime**

Keep as default

---

### Capping Application Level, Transaction Types, Number of Trips, Scheduled Start Date & Scheduled End Date

**Capping Application Level**

- [ ]  Customer
- [x]  Card
- Customer level allows a single customer to receive this capping product across multiple funding sources. Card Level restricts the product to one bucket per card.

**Transaction Types**

- [x]  Autoscan
- [x]  Variable
- [ ]  Flat
- Autoscan sets this to a contactless PAYG product (opposed to a retail fare), Variable is Tap on Tap off, Flat is no Tap off.

**Scheduled Start Date**

Select: `Immediately`

**Scheduled End Date**

Select: `Indefinite`

**NOTE:** If you want more information on what each of these fields mean, you can find more information here [How to create a capping product](https://www.notion.so/How-to-create-a-capping-product-a351fca899924dcaa1ccce4d342964fa?pvs=21)

## Step 4. Go to Zone Rules Page

### Field Breakdown

Zones Capping Enabled

- Turns Zone capping on

Peak / Off-peak Capping Preference

- This field determines the price a traveler will receive if they travel across a peak and off-peak period (tap on during off peak, tap off during on peak, vice-versa)

Zone Configuration

- This field is dependant on the structure of the zone network. In this case Brighton and Hove has a Non-concentric network. For more information on concentric vs non-concentric see: ‣

Schedule changes for the product

1. Select 'immediately'
2. Select ‘Indefinite’
3. Select ‘Save’

## Step 5. Configure Peak Zone Triangle

### Field Breakdown

Select Zones

Select: `'citySAVER'` & `'networkSAVER'`

Zone Triangle

1. `citySAVER to citySAVER` settings
    1. Cap Trigger = `6.5`
    2. Max Fare = `5.5`
    3. Select: `activate`
2. `citySAVER to networkSAVER` settings
    1. Cap Trigger = `7.5`
    2. Max Fare = `5.5`
    3. Select: `activate`
3. `networkSAVER` to `networkSAVER` settings
    1. Cap Trigger = `6.5`
    2. Max Fare = `5.5`
    3. Select: `activate`
4. Select: `Save`
    1. Select: `Immediate`
    2. Select `Indefinite`

## Step 6. Configure Off Peak Zone Triangle

### Field Breakdown

Select Zones

- Select `'citySAVER'` and `'networkSAVER'`

Zone Triangle

1. `citySAVER to citySAVER` settings
    1. Cap Trigger = `5.5`
    2. Max Fare = `5.5`
    3. Select: `activate`
2. `networkSAVER to networkSAVER` settings
    1. Cap Trigger = `5.5`
    2. Max Fare = `5.5`
    3. Select: `activate`
3. `citySAVER to networkSAVER` settings
    1. Cap Trigger = `6.5`
    2. Max Fare = `5.5`
    3. Select `activate`
4. Select: `Save`
    1. Select: `Immediate`
    2. Select `Indefinite`

## Step 7. Simulate taps

In order to simulate trips made by a traveller, Littlepay has provided a tap simulator.  To log in use:

Username `login`

Password `devicesimulator`

Make sure to select the `Littlepay Transaction` tab. Although the tap simulator looks complex and has a lot of fields, there are only 6 fields that should be altered when testing products: `1.Device`, `2.Auto Purchase Amount`, `3.Emv Primary Account Number`, `4.Transaction Date Time`, `5.Trip Route Identifier`, `6.Trip Zone Identifier`. The ways in which you can configure these fields is explored more in [How to simulate a tap](https://www.notion.so/How-to-simulate-a-tap-25d9bef91e9c44e1908f2312a2af856d?pvs=21).

Additionally, there is a simplified tap simulator in the merchant portal under the `Developer` tab on the left-hand sidebar that is called `Transaction Simulator`. This isn’t essential to test but might be worth getting your head around as some merchants might be using it.

## Step 8: Other capping types

Overall, there are four capping types that you can configure in the Merchant Portal. In addition to a `Daily Cap`, we have the `Time-based Cap`, `Multi-day Cap`, `Weekly Cap`. We will briefly cover how these vary functionally, but if you’re looking for why merchants use each of these caps you can find that information in [Capping types](https://www.notion.so/Capping-types-3d3bb1b311aa4e1197b4c646865bd905?pvs=21).

**Time-based Cap:** from the first tap, there is a set duration (X minutes) during which a traveler would have free transfers for a set number of trips (to the “trip limit”) or unlimited trips, based on the configuration.

Example: for a 90-minute time-based product, after being charged for the first tap, from that moment onward they will not be charged for any subsequent trips in the next 90 minutes.

**Multi-day Cap:** this is a rolling capping product, meaning that from the capping start time, a traveller will be capped for a set number of days in duration until the `Cap Trigger Amount` is reached.

Example: for a 3-day multi-day cap, if the multi-day capping product is set to start at 12:00pm, if a customer first taps on Monday past 12:00pm any fares till Thursday  12:00pm will contribute to this cap.

**Weekly Cap:** unlike the multi-day cap, this is set across the entirety of the week, where all of a customer’s fares will contribute to a weekly cap until the `Cap Trigger Amount` is reached, being reset every week.

Example: for a weekly cap, if a traveler taps on Monday at 00:00:00am, all of their fares will be contribute to the weekly cap until Sunday 23:59:59pm (these are the default start and end times for the capping period).

## Step 9: Fields unique to each capping type

**Daily Cap**

All Day

- This field checks whether all fares in one day will contribute to the daily cap (alternative is that a certain time period is set where caps would contribute)

Capping Period Overlap Time

- If All Day is enabled, this field will appear which allows an open capping product to continue into the next day. Applied capping products for one day will carry over into the next for the duration of the overlap time.

**Time-based Cap**

Capping Duration

- This is the amount of time (in minutes) that the capping period covers from the first tap.

Number of Transfers

- This is the amount of free transfers within the capping duration that are enabled once you reach the cap. It is defaulted to unlimited free transfers.

**Multi-day Cap**

Multi-Day Cap Number of Days

- This defines the length of the multi-day capping period (in days) from the first tap

Capping Start Time

- This is the time from which the multi-day capping period would be active. Only if you make your first tap after this start time will it create the multi-day cap. However, the end time is automatically calculated as X days from the first tap.

Number of Trips

- Similar to Time-based capping you can set the number of trips in this capping period that would qualify. This means that if the trip limit is reached, the capping product will no longer apply, irrespective of whether the duration (number of days) has expired.

**Weekly Cap**

Weekly Cap Start Day

- This can either be a Sunday or Monday and determines upon which day the weekly cap will start.

Capping Start and End Time

- This determines the time window for each day in which fares will count towards the cap limit.

This tutorial will revolve around the Brighton & Hove City SAVER product, which is live in production and can be found [here](https://www.buses.co.uk/flexi-fares).

### Step 1: Creating a MultiOperator Group

In order to create a MultiOperator Capping product, first you need to configure a MultiOperator Group. This  can be found on the left-hand sidebar of the Operations Portal titled `MultiOperator Groups`

The first thing to do is to “Add Group” which creates a row at the bottom of the list for you to give your MultiOperator group a name as well as to select which participants would fall into that group.

!https://s3-us-west-2.amazonaws.com/secure.notion-static.com/17581158-93db-43f1-a82c-5530b2949980/image-20220526-053519.png

- After you are happy with the participants selected you can click the save icon (note: you cannot edit the participant list after a MOC group has been created)
- It will display that there are “No products”. This is because products are assigned to the **participant** in the product settings located in `Capping` which will then assign it to the MultiOperator Group that holds that participant.

### Step 2: Creating a MultiOperator Capping product

The Operations Portal and Merchant Portal hold the same pricing and adjustment logic for their capping products. If you want to refresh yourself on the distinction between the different capping products refer to:

[Capping Tutorial - Basics (MP1)](https://www.notion.so/Capping-Tutorial-Basics-MP1-b8732928cef24886b61339db58c7d89c?pvs=21)

In saying this, there are a few key differences between the Operations Portal and Merchant Portal when it comes to creating a product, which are discussed as follows: 

Participants

- Here you can select which participant the product is active for
- If it’s not for a single participant, but a MultiOperator Group you have to click `YES` on the “Is this a multi-participant capping product?” field

Status

You have to set the ‘Status’ of the product when you create it

- For MultiOperator products: you can choose `active` or `inactive`
- For single participant products the only option will be  `inactive`

To demonstrate, we will be creating a capping product for the City SAVER fares whose configurations would look as follows in the operations portal:

### Step 3: Searching for a MultiOperator capping product

If you want to search for a MultiOperator Capping Product that has been created, you can do so in one of two ways. Either by 1. **searching by MultiOperator Group** or 2. **searching by Product**.

1. **Searching by MultiOperator group**

After creating a product and assigning it to all the participants in a MultiOperator group, you go to `MultiOperator Groups` tab on the left-hand sidebar.

Here you can see the products that fall under each of the MultiOperator Groups

- If you click on any of these product links, you can directly edit the product settings

**Example**

The product `Multi Operator Test - Variable CORAL` is assigned to the participants `firstbus-moc`, `STAGECOACH-VixTech`, and `goahead-moc`

In this case, the product would be part of the `Coral MOC POC`as all three participants make up this MultiOperator Group.

2. **Searching by product**

You can also search for the product by going directly to the `Capping`section on the left-hand sidebar and search for the product based on participant.

Note: because there are a lot of capping products stored in the test environment (displayed for every participant), this may take a bit of time to load.

### Step 4. Creating an incentive

Now we will recreate a Brighton & Hove incentive, which is currently live in production. We will be basing it on the marketing material they have provided:

To start with, you have to go to the `Product Summary` of an existing multi-day or weekly capping product (in our case CitySAVER is a weekly cap product) from the `Capping` tab on either the Merchant or Operations Portal. 

- From here, you navigate to the `Incentive Rules` section.

After clicking on the `Incentive Enabled` button it will reveal a whole range of configurations (as shown above).

- As CitySAVER has the `Daily Cap Discount` as the incentive type, we also have to create a Daily Cap product from which the discount will be taken.
- In this case, we see that on Day 1 for the City SAVER ticket, the trip is £5.50 which is the highest fare for the week, so we make a Daily Cap product with the following configurations:

Note: since B&H describe their flexible fares service as being “tap on, tap off contactless”, we have set the **Transaction Types** to `autoscan` and `variable`. The Daily Cap product should also be configured as a multi-participant capping product to work with the multi-day product.

**The fields in incentive options are broken down as follows:**

Incentive Type

!https://s3-us-west-2.amazonaws.com/secure.notion-static.com/29380ed5-f12f-490a-bc3a-941f7cf5fe00/image-20220602-053957.png

- `Daily Cap Discount` is available for both multi-day and weekly caps, allowing a user to travel x days in a capping period and qualify for a discount off the regular daily cap (for a set daily cap product). E.g. £0.27 discount off £5.50 limit making it a £5.23 limit
- `Cumulative Cap` is available only for weekly caps, allowing a user to spend no more than X amount in Y days. Both X and Y can be configured for any weekly cap. E.g. spend no more than £13 in 3 (non-consecutive) days, and no more than £20 in 5 (non-consecutive) days.

Daily Cap Product

- Here, you select the appropriate Daily Cap Product(s) upon which the incentives will be based on. Essentially, the incentives will detract from the cap limit by the discount amount specified.
- In our case we would select the `CitySAVER Daily Remake` product

This shows the Day 2 discount of £0.27, which is then deducted from the daily cap limit of £5.50.

Discount Type

- This determines how the discount will be applied. There is either `FLAT` which reduces the exact amount from the capping limit, or `PERCENTAGE` which reduces the set percentage of the fare from the capping limit.

### **Step 5a: Configuring a Daily Cap Discount**

**The fields in daily cap discounts are broken down as follows:**

Discount Qualifier

- This defines what is required to qualify for the discount: single trip or cap reached.
    - `Single Trip` provides a discount for each day you travel, irrespective of the fact whether you met the cap previously. This incentive encourages customers to travel more days throughout a week as you get a discount for each day you travel.
    - `Cap Reached` only provides a discount for the next day if the cap had been reached for the day prior. This incentive encourages customers to use public transport more throughout the day to reach the cap, and more days throughout the week, as you get a discount for the next day each time a customer reaches the cap.
    - **In our case:** `Cap Reached` is what is set for Brighton and Hove’s City SAVER product.
    

Configuration

- This is how the daily discounts section would be configured (currently, you can only select a Daily Table for the `Daily Cap Discount` option)

Daily Table Configuration

- This table will show the same amount of days as defined in the multi-day/weekly cap product (here is is a 7-day weekly cap)
- `Discount` is how much will be deducted from the capping limit (depending on whether it is `Flat` or `Percentage` )
- E.g. for a **cap limit of £5.50** with a **discount** **of £0.27** for day 2 and a **fare of £2.00**
    - This means that the cap limit is decreased to **£5.50 - £0.27 = £5.23,** therefore, the merchant portal would show **£2.00 of £5.23 limit.**
- `Description` describes the incentive for each day. This is what will show up on the Merchant Portal / Traveler Portal so it will be customer facing (this is the intended function, currently not working as expected).
- Note: if you have a route enabled/zone enabled for the daily cap the incentive will not apply. It relies on the daily cap working normally.

Here is how the Daily Table would be configured as per the Brighton and Hove CitySAVER requirements:

### **Step 5b: Configuring a Cumulative Cap**

There are two ways in which you can configure a cumulative cap 1. Daily Table, 2. Zone Triangle (as opposed to the Daily Cap Discount that just has the Daily Table).

1. **Daily Table**
- Here, you have the same discount qualifiers `Single Trip` and `Cap Reached`
- As discussed above, you configure the cap that applies after a set number of days. E.g. you would be capped £13 here across 3 days.

2. **Zone Triangle**

Days

- Select each day that you wish to apply an incentive to

Peak/Off Peak

- This is where you could select the peak and off-peak prices based on the pricing period applied to the participant. See more about pricing periods [here](https://www.notion.so/35e15a67afd94ed9971b4396c733bfbf?pvs=21)

Cap Trigger Amount

- ****Enter a new Cap limit for each zone combination you wish to apply it to

Max Fare Amount

- Enter a max fare amount of each zone combination you wish to apply it to

### **Step 6. Simulating MOC incentive taps**

- In order for the incentive to be applied for a MOC product, you need to ride across multiple participants in the same day (TOTO on one participant, then TOTO on another participant)
- However, you also need to make sure that the fare does not reach the cap trigger limit on the first participant (since, it needs to go across multiple operators to count the incentive, it deducts the discount from the fare that is after the first participant)
- Note: for the cap reached product, you have to have reached the cap in the previous day for the next day cap to apply

Here is an example of the daily cap discount being applied for our CitySAVER product (on the second participant `shingtest2`):

Customer ID: `80aac113-51e0-4054-8f64-1049f37b92d8`

PAN: `1234567890123436`

Here is an example of the daily cap discount being applied for the CitySAVER product (on the first participant `shingtest` ):

## Troubleshooting Guide

## The merchant has configured and enabled capping and/or discounts, but no transactions are qualifying or being adjusted by the products.

### **Possible Cause**

- The adjustments enabled field has not been set to ‘YES’ in the Payment Settings of the Operations portal.  More details to be found here:
- The merchant has not configured any pricing periods and has only configured peak period prices. The Peak period prices are only relevant if pricing periods are set. Otherwise pricing rules default to Off-Peak. Also, if no peak pricing periods are set the peak/off peak capping preference field is not relevant and has no impact on functionality.

[Required Settings to Enable Capping](https://www.notion.so/Required-Settings-to-Enable-Capping-1b6609d4734a4feabd10d0eabb615849?pvs=21)

## A customer has asked why their transaction didn’t qualify or adjusted by a product(s), what should I check?

### Possible Causes

- The incorrect zone id was assigned to the zone name on the zone page of the merchant portal. Please check the zone id from the tap message against the zone id in the portal.
- The nominal fare for the transaction has exceeded the ‘Max Fare Limit’. Please check the nominal fare of the transactions(s) against the ‘Nominal Fare Limit’ for the product or zones combination related to the transaction.
- The trip was ‘Incomplete’ and the ‘Incomplete Fare’ setting in the Merchant Portal is set to ‘Exclude from Capping’.

- The transaction occurred before or after the ‘Start’ or ‘End’ time of the product.
- Check if ‘Route capping’ is enabled. If so, check that the transaction occurred on the route included in the list of routes for the product.

## Most transactions qualify for ‘products’ but a few are not. All of the criteria have been met for the product.

### Possible Cause

- The tap message from the device is missing the zone ID for the tap on or off. This is an issue with the message coming from our device partner.

## I cannot refund a transaction

### Possible Causes

- The transaction is yet to be settled, a refund can’t be submitted until the transaction is settled.
- Ensure the ‘Enabled Refund ‘ Payment Settings is turned on and the Merchant hasn’t exceeded the Max refunds during the restriction period.

## My test taps are not coming through in the merchant portal, why might this be?

### **Possible Cause**

- In order for test taps to appear on the merchant portal in QA/Dev, the acquirer for this participant has to be set to LP
- Additionally, in order for test taps to occur the currency for QA/Dev has to be pounds (GBP)

## The Traveller Portal is only showing the last 14 days of a traveller’s transaction history

### **Possible Cause**

- The participant has to pay for the branded Traveller Portal
- If the above is true, then the ‘Selected Plan’ field in the Product Settings has to be set to BRANDED

## My Analytics page is not loading.

### **Possible Cause**

- The platform has a daily refresh scheduled for 6-7 pm (AESTD).
- If you are trying to access the Analytics page during that time please try again after the refresh.
- If you are trying to access the Analytics page outside of these hours please contact support@littlepay.com.

### The VAT (receipt) invoice is not showing up correctly

- If the selected plan on the Product Settings is not BASIC, the user can click the Edit symbol in the Receipt Generation modal to configure the receipt generation
- Receipt Generation, the fields should be configured as follows:
    - Enabled: Select ‘YES’ with the toggle switch
    - Business Trading Name: this should be formatted in the following format PARTICIPANT_ID-RECEIPT-TRADING-NAME
    - VAT Number: this should be provided by the merchant (does not affect the receipt generation logic)
    - Business ID: this should be provided by the merchant (does not affect the receipt generation logic)
    - Receipt Footer Text: this should be formatted in the following format PARTICIPANT_ID-RECEIPT-FOOTER

# Required Settings to Enable Capping

The following settings are required to be configured in order for capping to work.

## Operations Portal

### **Field Definitions:**

Adjustments enabled: If disabled to any ‘products’ configured in the customer's merchant portal

### Instructions

In the Operations portal:

- Go to the Participants List page
- Select the participant
- Go to the Payments Settings page
- Adjustments Enabled: Select ‘YES’ with the toggle switch.
- Incomplete Fares
    - Highest Cap Limit:

**************************************How to set-up a Traveller portal for a new merchant**************************************
Create a JIRA with the following template

| Transit Operator | Country | Merchant’s Existing Website | Required Languages | VAT Invoice | QA Participant ID | QA URL | PROD Participant ID | PROD URL | Branding Elements (Hex Colours) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | English
Other? Default? | Yes / No |  |  |  |  | Background colour: HEX CODE
Opposite or contrasting “Link” colour: HEX CODE
Contrasting “Heading” colour: HEX CODE |

Once we have the completed JIRA, we need to create another JIRA for a developer to implement the following

- Devops to create the subdomain in Dev and QA (ask in the #help slack channel)
- Create a CR for the subdomain change in prod. [Change Request guide](https://www.notion.so/Change-Request-guide-dc75eacae02f49c6a08583f12dbb2ec3?pvs=21)
    - Assign to team member from Devops who is on call for the week
- Configure the language (if required)
    - Add any new translations into Lokalise
- Implement colour and branding for that subdomain
"""


INITIAL_SYSTEM_PROMPT = """
You are a very helpful bot that is trying to answer questions or follow instructions for people working in a company called Littlepay. 
Answer questions based on the CONTEXT given, however do not say "based on the context provided" or similar when giving an answer, simply give the answer. 
If you do not know the answer and the CONTEXT doesn't contain the answer truthfully say "I don't know". Do not make up answers.

You may be given additional context to help answer questions. This will be labeled as SECONDARY CONTEXT. 
When any SECONDARY CONTEXT is provided you will use both the CONTEXT below to answer questions. 

CONTEXT:

Here is information about the Littlepay business, in markdown:
{littlepay_context}

SECONDARY CONTEXT:
{secondary_context}
"""

SECONDARY_CONTEXT_PROMPT = """
Forget any previously provided SECONDARY CONTEXT. Use the SECONDARY CONTEXT provided below to help answer questions. 

SECONDARY CONTEXT:
{secondary_context}
"""

SECONDARY_CONTEXTS = {
    'capping-discounts': SERVICE_OPS_HELP_CONTEXT
}

def get_context_setting_prompt():
    return INITIAL_SYSTEM_PROMPT.format(littlepay_context = SERVICE_OPS_HELP_CONTEXT, secondary_context = SERVICE_OPS_HELP_CONTEXT)

def get_available_secondary_contexts() -> str:
    return ", ".join(SECONDARY_CONTEXTS.keys())

def get_secondary_context_prompt(context_type) -> str:
    secondary_context = SECONDARY_CONTEXTS[context_type]
    return SECONDARY_CONTEXT_PROMPT.format(secondary_context = secondary_context)
