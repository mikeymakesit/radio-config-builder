class RadioFormat():
  brand   = 'Kenwood'
  model   = 'TH-D75'
  cpsName = 'RT Systems'

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
  'name'
]
