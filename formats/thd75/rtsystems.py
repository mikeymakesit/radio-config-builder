class RadioFormat():
  brand   = 'Kenwood'
  model   = 'TH-D75'
  cpsName = 'RT Systems'
  
  chanNameMaxlen = 14

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
    'dcs',
    'lockout',
    'step',
    'fineStepEnable',
    'fineStep',
    'digitalSquelch',
    'digitalCode',
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
      
      elif k == '':
        pass

      else:
        row[k] = getattr(c, k)
        
    return row
