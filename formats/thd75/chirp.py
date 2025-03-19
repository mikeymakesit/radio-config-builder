from math import floor

class RadioFormat():
  brand   = 'Kenwood'
  model   = 'TH-D75'
  cpsName = 'RT Systems'

  chanNameMaxlen = 14

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
    'dcs',
    'NN',
    'dcs',
    'crossMode'
    'modulation',
    'bandwidthKhz'
  ]

  def render_row(self, c: dict, n: int) -> dict:
    """ Given a row of channel data, return a dict formatted for this CPS """
    row = dict()
    for k in self.fieldOrder:

      if k == 'num':
        # Channel number
        row[k] = n
      
      elif k == 'offsetFreq':
        val = getattr(c,k)
        if val < 1.0:
          row[k] = str(floor((val * 1000.0))) + ' kHz'
        else:
          row[k] = str(val) + ' MHz'
      
      elif k == 'offsetDir':
        val = getattr(c,k)
        if val == '-':
          row[k] = 'Minus'
        elif val == '+':
          row[k] = 'Plus'
        else:
          row[k] = val.title()

      elif k == 'ctcssTx' or k == 'ctcssRx':
        row[k] = str(getattr(c,k)) + ' Hz'
      
      elif k == 'lockout':
        row[k] = getattr(c,k).title()
      
      elif k == 'toneMode':
          # None, Tone, T Sql
          val = getattr(c,k)
          if val == '':
            row[k] = 'None'
          elif val == 'tsql':
            row[k] = 't sql'.title()
          else:
            row[k] = val.title()
      
      elif k == 'stepKhz':
        row[k] = str(getattr(c,k)) + ' kHz'

      elif k == 'fineStepEnable':
        row[k] = getattr(c,k).title()
      
      elif k == 'fineStepHz':
        row[k] = str(getattr(c,k)) + ' Hz'

      elif k == 'dstarDigitalSquelch':
        row[k] = getattr(c,k).title()
      
      elif k == 'dstarDigitalCode':
        val = getattr(c,k).title()
        if val == '':
          row[k] = str(0)
        else:
          row[k] = val.title()

      else:
        row[k] = getattr(c,k)
        
    return row
