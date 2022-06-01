from . import yfinance as yf
import time, sys, argparse

	

def ticker_tofiles(ticker, outdir, **kwargs):

	tick = yf.Ticker(ticker)
	
	unprotected_attrs = {
		'actions':'DataFrame', 
		'analysis' : 'DataFrame',
		'balance_sheet' : 'DataFrame',
		'balancesheet' : 'DataFrame',
		'calendar' : 'DataFrame',
		'cashflow' : 'DataFrame',
		'dividends' : 'Series',
		'earnings' : 'DataFrame',
		'financials' : 'DataFrame',
		'info' : 'dict',
		'institutional_holders' : 'DataFrame',
		'major_holders' : 'DataFrame',
		'mutualfund_holders' : 'DataFrame',
		'news' : 'list',
		'options' : 'tuple',
		'quarterly_balance_sheet' : 'DataFrame',
		'quarterly_balancesheet' : 'DataFrame',
		'quarterly_cashflow' : 'DataFrame',
		'quarterly_earnings' : 'DataFrame',
		'quarterly_financials' : 'DataFrame',
		'recommendations' : 'DataFrame',
		'shares' : 'DataFrame',
		'sustainability' : 'DataFrame',
		'ticker' : 'str',
	}

	for attr, typ in unprotected_attrs.items():
		if typ in ['DataFrame', 'Series']:
			getattr(tick, attr).to_csv(outdir+time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime(time.time()))+"_"+ticker+"_"+attr+'.csv')
		else:
			f = open(outdir+time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime(time.time()))+"_"+ticker+"_"+attr+'.out', 'w')
			f.write(str(getattr(tick, attr)))
			f.close()










