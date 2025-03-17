from typing import Optional
from pydantic import BaseModel, RootModel, ConfigDict

class ChannelEntry(BaseModel):
  model_config = ConfigDict(
    str_strip_whitespace=True,
    validate_assignment=True
  )
  name: str
  freq: Optional[str]
  freqRx: Optional[float] = 146.520
  freqTx: Optional[float] = 146.520
  modulation: Optional[str] = "FM"
  offsetFreq: Optional[float] = 0.0
  offsetDir: Optional[str] = ""
  memGrpName: Optional[str] = ""
  memGrpNum: Optional[int] = 0
  toneMode: Optional[str] = ""
  ctcssTx: Optional[float] = 67.0
  ctcssRx: Optional[float] = 67.0
  dcs: Optional[int] = 23
  lockout: Optional[str] = "Off"
  step: Optional[str] = ""
  fineStepEnable: Optional[str] = ""
  fineStep: Optional[str] = ""
  digitalSquelch: Optional[str] = ""
  digitalCode: Optional[int] = 0
  yourCall: Optional[str] = ""
  rpt1Call: Optional[str] = ""
  rpt2Call: Optional[str] = ""
  comment: Optional[str] = ""

class ChannelData(RootModel):
  root: list[ChannelEntry]
