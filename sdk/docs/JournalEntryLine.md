# JournalEntryLine

A Journal Entry line entity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_date** | **datetime** | The Journal Entry Line accounting date. | 
**activity_date** | **datetime** | The actual date of the activity. Differs from the accounting date when creating journals that would occur in a closed period. | 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**instrument_id** | **str** | To indicate the instrument of the transaction that the Journal Entry Line posted for, if applicable. | 
**instrument_scope** | **str** | The scope in which the Journal Entry Line instrument is in. | 
**sub_holding_keys** | [**dict(str, PerpetualProperty)**](PerpetualProperty.md) | The sub-holding properties which are part of the AccountingKey. | [optional] 
**tax_lot_id** | **str** | The tax lot Id that the Journal Entry Line is impacting. | 
**general_ledger_account_code** | **str** | The code of the account in the general ledger the Journal Entry was posted to. | 
**local** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**base** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**posting_module_code** | **str** | The code of the posting module where the posting rules derived the Journal Entry lines. | [optional] 
**posting_rule** | **str** | The rule generating the Journal Entry Line. | 
**as_at_date** | **datetime** | The corresponding input date and time of the Transaction generating the Journal Entry Line. | 
**activities_description** | **str** | This would be the description of the business activities this Journal Entry Line is for. | [optional] 
**source_type** | **str** | So far are 4 types: LusidTxn, LusidValuation, Manual and External. | 
**source_id** | **str** | For the Lusid Source Type this will be the txn Id. For the rest will be what the user populates. | 
**properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | A set of properties for the Abor. | [optional] 
**movement_name** | **str** | The name of the movement. | 
**holding_type** | **str** | Defines the broad category holding within the portfolio. | 
**economic_bucket** | **str** | Raw Journal Entry Line details of the economic bucket for the Journal Entry Line. | 
**levels** | **list[str]** | Resolved data from the general ledger profile where the GeneralLedgerProfileCode is specified in the GetJournalEntryLines request body. | [optional] 
**source_levels** | **list[str]** | Source data from the general ledger profile where the GeneralLedgerProfileCode is specified in the GetJournalEntryLines request body. | [optional] 
**links** | [**list[Link]**](Link.md) | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

