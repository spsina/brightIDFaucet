from core.constraints.abstract import ConstraintParam, ConstraintVerification, ConstraintApp
from core.utils import Web3Utils, InvalidAddressException
from rest_framework.exceptions import ValidationError
from core.constants import GLM_ABI



class GLMStakingVerification(ConstraintVerification):
    app_name = ConstraintApp.GLM_STAKING.value

    _param_keys = [
        ConstraintParam.CHAIN,
        ConstraintParam.MINIMUM,
    ]
    GLM_CONTRACT_ADDRESS = "0x879133Fd79b7F48CE1c368b0fCA9ea168eaF117c"

    def __init__(self, user_profile) -> None:
        super().__init__(user_profile)

    def is_observed(self, *args, **kwargs):
        from core.models import Chain

        chain_pk = self.param_values[ConstraintParam.CHAIN.name]
        
        minimum = self.param_values[ConstraintParam.MINIMUM.name]

        chain = Chain.objects.get(pk=chain_pk)
        web3_utils = Web3Utils(chain.rpc_url_private, chain.poa)


        staked_amount = 0
        try:
            for wallet in self.user_addresses:
                staked_amount += self.get_staked_amount(wallet, web3_utils) 
                
        except InvalidAddressException as e:
            raise ValidationError({"address": str(e)})
        
        return staked_amount >= minimum

    def get_staked_amount(self, user_address: str, web3_utils: Web3Utils) -> int:
        web3_utils.set_contract(self.GLM_CONTRACT_ADDRESS, GLM_ABI)
        deposits_function = web3_utils.contract.functions.deposits(user_address)
        return web3_utils.contract_call(deposits_function)

