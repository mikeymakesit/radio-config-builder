from math import floor

class RadioFormat():
  brand   = 'Kenwood'
  model   = 'TH-D75'
  cpsName = 'RT Systems'

  chanNameMaxlen = 16

  # Headers and examples from exported CSV:
  # Location,Name,Frequency,Duplex,Offset,Tone,rToneFreq,cToneFreq,DtcsCode,DtcsPolarity,RxDtcsCode,CrossMode,Mode,TStep,Skip,Power,Comment,URCALL,RPT1CALL,RPT2CALL,DVCODE
  # 0,2m Call,146.520000,,0.600000,,88.5,88.5,023,NN,023,Tone->Tone,FM,5.00,,50W,,,,,
  # 1,70cm Call,446.000000,,5.000000,,88.5,88.5,023,NN,023,Tone->Tone,FM,25.00,,50W,,,,,
  # 2,WW7PSR,146.960000,-,0.600000,TSQL,103.5,103.5,023,NN,023,Tone->Tone,FM,5.00,,50W,,,,,
  fieldOrder = [
    'num',
    'name',
    'freqRx',
    'offsetDir',
    'offsetFreq',
    'toneMode',
    'ctcssTx',
    'ctcssRx',
    'dcsTx',
    'dcsPolarity',
    'dcsRx',
    'crossMode',
    'modulation',
    'stepKhz',
    'lockout',
    'txPowerW',
    'comment',
    'yourCall',
    'rpt1Call',
    'rpt2Call',
    'dstarDigitalCode'
  ]

  def render_row(self, c: dict, n: int) -> dict:
    """ Given a row of channel data, return a dict formatted for this CPS """
    row = dict()
    for k in self.fieldOrder:
      if k != 'num':
        val = getattr(c,k)

      if k == 'num':
        # Channel number
        row[k] = n
      
      elif k == 'name':
        row[k] = val[:self.chanNameMaxlen]
      
      elif k == 'offsetDir':
        if val == 'simplex':
          row[k] = ''
        else:
          row[k] = val

      elif k == 'toneMode':
          if val == 'tsql':
            row[k] = val.upper()
          elif val in ['tone', 'cross']:
            row[k] = val.title()
          else:
            row[k] = val
      
      elif k == 'stepKhz':
        row[k] = float(val)
      
      elif k == 'lockout':
        if val == "on":
          row[k] = 'S'
        else:
          row[k] = ''
      
      elif k == 'txPowerW':
        row[k] = str(floor(val)) + 'W'
      
      elif k == 'dstarDigitalCode':
        row[k] = val.title()

      else:
        row[k] = val
        
    return row
