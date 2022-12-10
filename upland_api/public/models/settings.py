from typing import Any, List, Optional
from pydantic import BaseModel, Field


class YieldBatch(BaseModel):
    interval: int
    size: int


class Features(BaseModel):
    treasures: List[int]
    standard_treasure: List[int]
    collections: List[int]
    riot_mode: List[int]
    construction: List[int]
    nft_swap: List[str]


class FiatSale(BaseModel):
    min_price: int
    max_price: int
    warning_price: int
    wire_transfer_min_price: int


class GlobalLightingItem(BaseModel):
    type: Optional[str] = None
    position: List[float]
    intensity: float
    color: str


class Car(BaseModel):
    field_0: int = Field(..., alias="0")
    field_1: int = Field(..., alias="1")
    field_2: int = Field(..., alias="2")


class Building(BaseModel):
    field_0: int = Field(..., alias="0")
    field_1: int = Field(..., alias="1")
    field_2: int = Field(..., alias="2")


class PropertyModel(BaseModel):
    zoom_level: int
    car: Car
    building: Building


class ActionsToShowCaptcha(BaseModel):
    buyFromUpland: bool
    makeOffer: bool
    instantBuy: bool
    registrationInStorePromo: bool
    purchaseInStorePromo: bool
    login: bool
    signup: bool
    nftSwapOffer: bool
    registrationInPrimaryMarket: bool
    purchaseInPrimaryMarketEarlySale: bool
    purchaseInPrimaryMarketLimitedSale: bool
    purchaseInPrimaryMarketUnlimitedSale: bool
    purchaseInNftShop: bool
    purchaseInEssentialsShop: bool
    transferUpx: bool
    sparkStreakCollect: bool
    sparkStreakCheckIn: bool
    purchaseInFootballEssentialsShop: bool
    developersPortalApiLogin: bool
    developersPortalApiSignUp: bool
    developersPortalApiChangePassword: bool
    registrationInFootballPrimaryMarket: bool
    purchaseInFootballPrimaryMarketEarlySale: bool
    purchaseInFootballPrimaryMarketLimitedSale: bool
    purchaseInFootballPrimaryMarketUnlimitedSale: bool


class PropertyFiatSellCooldownHours(BaseModel):
    field_1: int = Field(..., alias="1")
    field_2: int = Field(..., alias="2")
    field_3: int = Field(..., alias="3")
    field_4: int = Field(..., alias="4")
    field_5: int = Field(..., alias="5")


class PropertyFiatBuyPriceLimit(BaseModel):
    account_age_in_days: int
    price_limit: int


class Field0(BaseModel):
    name: str
    networth_from: int
    networth_to: int


class Field1(BaseModel):
    name: str
    networth_from: int
    networth_to: int


class Field2(BaseModel):
    name: str
    networth_from: int
    networth_to: int


class Field3(BaseModel):
    name: str
    networth_from: int
    networth_to: int


class Field4(BaseModel):
    name: str
    networth_from: int
    networth_to: int


class Field5(BaseModel):
    name: str
    networth_from: int
    networth_to: Any


class UserLevels(BaseModel):
    field_0: Field0 = Field(..., alias="0")
    field_1: Field1 = Field(..., alias="1")
    field_2: Field2 = Field(..., alias="2")
    field_3: Field3 = Field(..., alias="3")
    field_4: Field4 = Field(..., alias="4")
    field_5: Field5 = Field(..., alias="5")


class FsaPropertyFiatSellCooldownHours(BaseModel):
    field_1: int = Field(..., alias="1")
    field_2: int = Field(..., alias="2")
    field_3: int = Field(..., alias="3")
    field_4: int = Field(..., alias="4")
    field_5: int = Field(..., alias="5")


class GetConfigOK(BaseModel):
    spark_token_contract: str
    nft_token_contract: str
    eos_upld_contract: str
    producer: str
    contract: str
    token_contract: str
    yield_batch: YieldBatch
    show_video_tutorial: bool
    features: Features
    fiat_sale: FiatSale
    global_lighting: List[GlobalLightingItem]
    property_model: PropertyModel
    properties_on_fiat_sale_limit: int
    actions_to_show_captcha: ActionsToShowCaptcha
    use_new_payment_plugin: bool
    property_fiat_sell_cooldown_hours: PropertyFiatSellCooldownHours
    property_fiat_buy_price_limit: PropertyFiatBuyPriceLimit
    user_levels: UserLevels
    enabled_features: Any
    fsa_property_fiat_sell_cooldown_hours: FsaPropertyFiatSellCooldownHours
    fsa_first_purchase_daily_limit: int
    fsa_first_purchase_lifetime_limit: int
    transfer_upx_commission: str
    transfer_upx_minimum_amount: str
    transfer_upx_minimum_account_age: int
    transfer_upx_date_range: int
    put_for_sale_threshold_rate: str
    minting_cooldown_seconds: int


class GetMaintenanceOK(BaseModel):
    is_under_maintenance: bool
