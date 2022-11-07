import { ReactComponent as CarIcon } from "../assets/svg/info.svg";

type Props = {
  //color_id: number,
  rate: number // 駐車率
}

const return_color = (rate: number) => {

  // 車のアイコンのカラー一覧
  const IconColor = ['#00bfa5', '#f57f17', '#b71c1c'];

  if (rate === undefined) {
    return IconColor[0];
  } else {
    if (rate < 50) {
      return IconColor[0];
    } else if (50 <= rate && rate < 80) {
      return IconColor[1];
    } else if (rate >= 80) {
      return IconColor[2];
    }
  }
};

const ParkingInfo = (props: Props) => {
  const color: string | undefined = return_color(props.rate);
  
  return ( 
    <div> 
      <CarIcon style={{ fill: color }}></CarIcon>
      <p className="font-mono text-center m-20 text-5xl">{props.rate}%</p>
    </div>
  );
};

export default ParkingInfo