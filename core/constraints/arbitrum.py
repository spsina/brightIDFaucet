from core.constraints.abstract import (
    ConstraintApp,
    ConstraintParam,
    ConstraintVerification,
)
from core.thirdpartyapp.arbitrum_bridge import ArbitrumBridgeUtils


class HasBridgedToken(ConstraintVerification):
    _param_keys = [
        ConstraintParam.ADDRESS,
        ConstraintParam.MINIMUM,
        ConstraintParam.SOURCE_CHAIN,
        ConstraintParam.DESTINATION_CHAIN,
    ]
    app_name = ConstraintApp.ARBITRUM.value

    def __init__(self, user_profile) -> None:
        super().__init__(user_profile)

    def is_observed(self, *args, **kwargs) -> bool:
        minimum_amount = int(self.param_values[ConstraintParam.MINIMUM.name])
        sourec_chain = self.param_values[ConstraintParam.SOURCE_CHAIN.name]
        # dest_chain = self.param_values[ConstraintParam.DESTINATION_CHAIN.name]
        token_address = self.param_values[ConstraintParam.ADDRESS.name]

        arb_utils = ArbitrumBridgeUtils()

        if token_address.lower() in ["eth", ""]:
            token_address = None

        user_wallets = self.user_addresses
        for wallet in user_wallets:
            if sourec_chain == "any":
                bridging_results = arb_utils.check_all_bridge_transactions(
                    wallet, token_address, minimum_amount
                )
                if any(bridging_results.values()):
                    return True
            else:
                source_chain, target_chain = self._parse_chain(sourec_chain)
                if arb_utils.check_bridge_transactions(
                    wallet, token_address, minimum_amount, source_chain, target_chain
                ):
                    return True

        return False

    def _parse_chain(self, chain):
        chain_mapping = {
            "ethereum_to_arbitrum": ("ethereum", "arbitrum"),
            "arbitrum_to_ethereum": ("arbitrum", "ethereum"),
            "arbitrum_to_nova": ("arbitrum", "nova"),
            "nova_to_arbitrum": ("nova", "arbitrum"),
        }
        if chain not in chain_mapping:
            raise ValueError(f"Invalid chain parameter: {chain}")
        return chain_mapping[chain]
