type Props = {
  label: string
  onClick: () => void
}

export const Button = ({label, onClick}: Props) => (
  <button onClick={onClick}>
    {label}
  </button>
)
