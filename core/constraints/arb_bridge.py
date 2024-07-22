from django.db.models.functions import Lower

from core.constraints.abstract import (
    ConstraintApp,
    ConstraintParam,
    ConstraintVerification,
)
from core.thirdpartyapp import Subgraph


class BridgeEthToArb(ConstraintVerification):
    _param_keys = [
        ConstraintParam.MINIMUM,
    ]
    app_name = ConstraintApp.ARB_BRIDGE.value

    def __init__(self, user_profile) -> None:
        super().__init__(user_profile)

    def is_observed(self, *args, **kwargs) -> bool:
        try:
            min_amount = self.param_values[ConstraintParam.MINIMUM.name]
            return self.has_bridged(min_amount)
        except Exception:
            pass
        return False

    def has_bridged(self, min_amount):
        subgraph = Subgraph()

        user_wallets = self.user_profile.wallets.values_list(
            Lower("address"), flat=True
        )

        query = """
        query GetMessageDelivereds($wallets: [String]) {
            messageDelivereds(
                where: {
                    txOrigin_in: $wallets
                    kind: 12
                }
            ) {
                id
                transactionHash
            }
        }
        """
        vars = {
            "wallets": list(user_wallets),
        }

        res = subgraph.send_post_request(
            subgraph.path.get("arb_bridge_mainnet"), query=query, vars=vars
        )
        match res:
            case None:
                return False
            case {"data": {"messageDelivereds": messages}} if len(
                messages
            ) >= min_amount:
                return True
            case _:
                return False
