from math import floor

class RadioFormat():
  brand   = 'Kenwood'
  model   = 'TH-D75'
  cpsName = 'RT Systems'

  chanNameMaxlen = 16

  # Headers from exported CSV:
  # Channel Number,Receive Frequency,Transmit Frequency,Offset Frequency,
  # Offset Direction,Operating Mode,Name,Tone Mode,CTCSS,Rx CTCSS,DCS,Lockout,
  # Step,Fine Step Enable,Fine Step,Digital Squelch,Digital Code,Your Callsign,
  # Rpt-1 CallSign,Rpt-2 CallSign,Group,Comment
  fieldOrder = [
    'num',
    'freqRx',
    'freqTx',
    'offsetFreq',
    'offsetDir',
    'modulation',
    'name',
    'toneMode',
    'ctcssTx',
    'ctcssRx',
    'dcsTx',
    'lockout',
    'stepKhz',
    'fineStepEnable',
    'fineStepHz',
    'dstarDigitalSquelch',
    'dstarDigitalCode',
    'yourCall',
    'rpt1Call',
    'rpt2Call',
    'memGrpName',
    'comment'
  ]

  def render_row(self, c: dict, n: int) -> dict:
    """ Given a row of channel data, return a dict formatted for this CPS """
    row = dict()
    for k in self.fieldOrder:

      if k == 'num':
        # Channel number
        row[k] = n
      
      elif k == 'name':
        row[k] = getattr(c,k)[:self.chanNameMaxlen]
      
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
