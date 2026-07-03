class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        # Used answer to store earliest finish time.
        answer = float("inf")

        # Tried every land ride.
        for i in range(len(landStartTime)):

            # Tried every water ride.
            for j in range(len(waterStartTime)):

                # Calculated finish time of land ride.
                landFinish = landStartTime[i] + landDuration[i]

                # Calculated actual start time of water ride.
                waterStart = max(waterStartTime[j], landFinish)

                # Updated answer for land then water.
                answer = min(
                    answer,
                    waterStart + waterDuration[j]
                )

                # Calculated finish time of water ride.
                waterFinish = waterStartTime[j] + waterDuration[j]

                # Calculated actual start time of land ride.
                landStart = max(landStartTime[i], waterFinish)

                # Updated answer for water then land.
                answer = min(
                    answer,
                    landStart + landDuration[i]
                )

        # Returned earliest possible finish time.
        return answer