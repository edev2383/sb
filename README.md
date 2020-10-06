# Stockbox

Stockbox is an equity testing suite that scrapes yahoo finance for ticker data. Returns a dataframe and calculates indicators

Docs to come...

Rules (note for later):
RuleParser breaks a statement
> [Close(3)] < [SMA(5) * 1.02] 

down to the following dictionary:
'''
{ 
  focus: { 
        key: Close,
        from_index: 3,
        },
  operator: >,
  comparison: {
        key: SMA(5)
        from_index: 0,
        extension: {
                operator: *
                value: 1.02
                }
        }
}
'''

Todos - 
- Reorg modules
