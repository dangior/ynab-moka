# ynab-moka

This is a python client for YNAB API. Initial commit April 2020

Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import ynab_moka 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ynab_moka
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import ynab_moka
from ynab_moka.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = ynab_moka.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = ynab_moka.AccountsApi(ynab_moka.ApiClient(configuration))
budget_id = 'budget_id_example' # str | The id of the budget (\"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget)
account_id = 'account_id_example' # str | The id of the account

try:
    # Single account
    api_response = api_instance.get_account_by_id(budget_id, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_account_by_id: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.youneedabudget.com/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountsApi* | [**get_account_by_id**](docs/AccountsApi.md#get_account_by_id) | **GET** /budgets/{budget_id}/accounts/{account_id} | Single account
*AccountsApi* | [**get_accounts**](docs/AccountsApi.md#get_accounts) | **GET** /budgets/{budget_id}/accounts | Account list
*BudgetsApi* | [**get_budget_by_id**](docs/BudgetsApi.md#get_budget_by_id) | **GET** /budgets/{budget_id} | Single budget
*BudgetsApi* | [**get_budget_settings_by_id**](docs/BudgetsApi.md#get_budget_settings_by_id) | **GET** /budgets/{budget_id}/settings | Budget Settings
*BudgetsApi* | [**get_budgets**](docs/BudgetsApi.md#get_budgets) | **GET** /budgets | List budgets
*CategoriesApi* | [**get_categories**](docs/CategoriesApi.md#get_categories) | **GET** /budgets/{budget_id}/categories | List categories
*CategoriesApi* | [**get_category_by_id**](docs/CategoriesApi.md#get_category_by_id) | **GET** /budgets/{budget_id}/categories/{category_id} | Single category
*CategoriesApi* | [**get_month_category_by_id**](docs/CategoriesApi.md#get_month_category_by_id) | **GET** /budgets/{budget_id}/months/{month}/categories/{category_id} | Single category for a specific budget month
*CategoriesApi* | [**update_month_category**](docs/CategoriesApi.md#update_month_category) | **PATCH** /budgets/{budget_id}/months/{month}/categories/{category_id} | Update a category for a specific month
*DeprecatedApi* | [**bulk_create_transactions**](docs/DeprecatedApi.md#bulk_create_transactions) | **POST** /budgets/{budget_id}/transactions/bulk | Bulk create transactions
*MonthsApi* | [**get_budget_month**](docs/MonthsApi.md#get_budget_month) | **GET** /budgets/{budget_id}/months/{month} | Single budget month
*MonthsApi* | [**get_budget_months**](docs/MonthsApi.md#get_budget_months) | **GET** /budgets/{budget_id}/months | List budget months
*PayeeLocationsApi* | [**get_payee_location_by_id**](docs/PayeeLocationsApi.md#get_payee_location_by_id) | **GET** /budgets/{budget_id}/payee_locations/{payee_location_id} | Single payee location
*PayeeLocationsApi* | [**get_payee_locations**](docs/PayeeLocationsApi.md#get_payee_locations) | **GET** /budgets/{budget_id}/payee_locations | List payee locations
*PayeeLocationsApi* | [**get_payee_locations_by_payee**](docs/PayeeLocationsApi.md#get_payee_locations_by_payee) | **GET** /budgets/{budget_id}/payees/{payee_id}/payee_locations | List locations for a payee
*PayeesApi* | [**get_payee_by_id**](docs/PayeesApi.md#get_payee_by_id) | **GET** /budgets/{budget_id}/payees/{payee_id} | Single payee
*PayeesApi* | [**get_payees**](docs/PayeesApi.md#get_payees) | **GET** /budgets/{budget_id}/payees | List payees
*ScheduledTransactionsApi* | [**get_scheduled_transaction_by_id**](docs/ScheduledTransactionsApi.md#get_scheduled_transaction_by_id) | **GET** /budgets/{budget_id}/scheduled_transactions/{scheduled_transaction_id} | Single scheduled transaction
*ScheduledTransactionsApi* | [**get_scheduled_transactions**](docs/ScheduledTransactionsApi.md#get_scheduled_transactions) | **GET** /budgets/{budget_id}/scheduled_transactions | List scheduled transactions
*TransactionsApi* | [**create_transaction**](docs/TransactionsApi.md#create_transaction) | **POST** /budgets/{budget_id}/transactions | Create a single transaction or multiple transactions
*TransactionsApi* | [**get_transaction_by_id**](docs/TransactionsApi.md#get_transaction_by_id) | **GET** /budgets/{budget_id}/transactions/{transaction_id} | Single transaction
*TransactionsApi* | [**get_transactions**](docs/TransactionsApi.md#get_transactions) | **GET** /budgets/{budget_id}/transactions | List transactions
*TransactionsApi* | [**get_transactions_by_account**](docs/TransactionsApi.md#get_transactions_by_account) | **GET** /budgets/{budget_id}/accounts/{account_id}/transactions | List account transactions
*TransactionsApi* | [**get_transactions_by_category**](docs/TransactionsApi.md#get_transactions_by_category) | **GET** /budgets/{budget_id}/categories/{category_id}/transactions | List category transactions
*TransactionsApi* | [**get_transactions_by_payee**](docs/TransactionsApi.md#get_transactions_by_payee) | **GET** /budgets/{budget_id}/payees/{payee_id}/transactions | List payee transactions
*TransactionsApi* | [**update_transaction**](docs/TransactionsApi.md#update_transaction) | **PUT** /budgets/{budget_id}/transactions/{transaction_id} | Updates an existing transaction
*TransactionsApi* | [**update_transactions**](docs/TransactionsApi.md#update_transactions) | **PATCH** /budgets/{budget_id}/transactions | Update multiple transactions
*UserApi* | [**get_user**](docs/UserApi.md#get_user) | **GET** /user | User info


## Documentation For Models

 - [Account](docs/Account.md)
 - [AccountResponse](docs/AccountResponse.md)
 - [AccountResponseData](docs/AccountResponseData.md)
 - [AccountsResponse](docs/AccountsResponse.md)
 - [AccountsResponseData](docs/AccountsResponseData.md)
 - [BudgetDetail](docs/BudgetDetail.md)
 - [BudgetDetailResponse](docs/BudgetDetailResponse.md)
 - [BudgetDetailResponseData](docs/BudgetDetailResponseData.md)
 - [BudgetSettings](docs/BudgetSettings.md)
 - [BudgetSettingsResponse](docs/BudgetSettingsResponse.md)
 - [BudgetSettingsResponseData](docs/BudgetSettingsResponseData.md)
 - [BudgetSummary](docs/BudgetSummary.md)
 - [BudgetSummaryResponse](docs/BudgetSummaryResponse.md)
 - [BudgetSummaryResponseData](docs/BudgetSummaryResponseData.md)
 - [BulkResponse](docs/BulkResponse.md)
 - [BulkResponseData](docs/BulkResponseData.md)
 - [BulkResponseDataBulk](docs/BulkResponseDataBulk.md)
 - [BulkTransactions](docs/BulkTransactions.md)
 - [CategoriesResponse](docs/CategoriesResponse.md)
 - [CategoriesResponseData](docs/CategoriesResponseData.md)
 - [Category](docs/Category.md)
 - [CategoryGroup](docs/CategoryGroup.md)
 - [CategoryGroupWithCategories](docs/CategoryGroupWithCategories.md)
 - [CategoryResponse](docs/CategoryResponse.md)
 - [CategoryResponseData](docs/CategoryResponseData.md)
 - [CurrencyFormat](docs/CurrencyFormat.md)
 - [DateFormat](docs/DateFormat.md)
 - [ErrorDetail](docs/ErrorDetail.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [HybridTransaction](docs/HybridTransaction.md)
 - [HybridTransactionsResponse](docs/HybridTransactionsResponse.md)
 - [HybridTransactionsResponseData](docs/HybridTransactionsResponseData.md)
 - [MonthDetail](docs/MonthDetail.md)
 - [MonthDetailResponse](docs/MonthDetailResponse.md)
 - [MonthDetailResponseData](docs/MonthDetailResponseData.md)
 - [MonthSummariesResponse](docs/MonthSummariesResponse.md)
 - [MonthSummariesResponseData](docs/MonthSummariesResponseData.md)
 - [MonthSummary](docs/MonthSummary.md)
 - [Payee](docs/Payee.md)
 - [PayeeLocation](docs/PayeeLocation.md)
 - [PayeeLocationResponse](docs/PayeeLocationResponse.md)
 - [PayeeLocationResponseData](docs/PayeeLocationResponseData.md)
 - [PayeeLocationsResponse](docs/PayeeLocationsResponse.md)
 - [PayeeLocationsResponseData](docs/PayeeLocationsResponseData.md)
 - [PayeeResponse](docs/PayeeResponse.md)
 - [PayeeResponseData](docs/PayeeResponseData.md)
 - [PayeesResponse](docs/PayeesResponse.md)
 - [PayeesResponseData](docs/PayeesResponseData.md)
 - [SaveCategoryResponse](docs/SaveCategoryResponse.md)
 - [SaveCategoryResponseData](docs/SaveCategoryResponseData.md)
 - [SaveMonthCategory](docs/SaveMonthCategory.md)
 - [SaveMonthCategoryWrapper](docs/SaveMonthCategoryWrapper.md)
 - [SaveSubTransaction](docs/SaveSubTransaction.md)
 - [SaveTransaction](docs/SaveTransaction.md)
 - [SaveTransactionWrapper](docs/SaveTransactionWrapper.md)
 - [SaveTransactionsResponse](docs/SaveTransactionsResponse.md)
 - [SaveTransactionsResponseData](docs/SaveTransactionsResponseData.md)
 - [SaveTransactionsWrapper](docs/SaveTransactionsWrapper.md)
 - [ScheduledSubTransaction](docs/ScheduledSubTransaction.md)
 - [ScheduledTransactionDetail](docs/ScheduledTransactionDetail.md)
 - [ScheduledTransactionResponse](docs/ScheduledTransactionResponse.md)
 - [ScheduledTransactionResponseData](docs/ScheduledTransactionResponseData.md)
 - [ScheduledTransactionSummary](docs/ScheduledTransactionSummary.md)
 - [ScheduledTransactionsResponse](docs/ScheduledTransactionsResponse.md)
 - [ScheduledTransactionsResponseData](docs/ScheduledTransactionsResponseData.md)
 - [SubTransaction](docs/SubTransaction.md)
 - [TransactionDetail](docs/TransactionDetail.md)
 - [TransactionResponse](docs/TransactionResponse.md)
 - [TransactionResponseData](docs/TransactionResponseData.md)
 - [TransactionSummary](docs/TransactionSummary.md)
 - [TransactionsResponse](docs/TransactionsResponse.md)
 - [TransactionsResponseData](docs/TransactionsResponseData.md)
 - [UpdateTransaction](docs/UpdateTransaction.md)
 - [UpdateTransactionsWrapper](docs/UpdateTransactionsWrapper.md)
 - [User](docs/User.md)
 - [UserResponse](docs/UserResponse.md)
 - [UserResponseData](docs/UserResponseData.md)


## Documentation For Authorization


## bearer

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author



